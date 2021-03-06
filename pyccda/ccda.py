"""A basic CCDA library for Python.

  Usage:
    import pyccda
    ccda = pyccda.CcdaDocument(<File pointer to a CCDA XML file.>)
    ccda.to_message()  # Returns CCDA represented as a ProtoRPC message.
    ccda.to_csv()  # Returns CCDA represented as a CSV.
"""

from xml.dom import minidom
import cStringIO
import csv
import datetime
import messages
from protorpc import protojson


class Root(object):
  """The "root" attribute of templateId elements."""
  ALLERGY = '2.16.840.1.113883.10.20.22.4.7'
  ALLERGY_REACTION = '2.16.840.1.113883.10.20.22.4.9'
  ALLERGY_SEVERITY = '2.16.840.1.113883.10.20.22.4.8'
  ALLERGY_STATUS = '2.16.840.1.113883.10.20.22.4.28'
  ENCOUNTER = '2.16.840.1.113883.10.20.22.4.49'
  IMMUNIZATION = '2.16.840.1.113883.10.20.22.2.2.1'
  IMMUNIZATION_PRODUCT = '2.16.840.1.113883.10.20.22.4.54'
  LAB = '2.16.840.1.113883.10.20.22.2.3.1'
  MEDICATION = '2.16.840.1.113883.10.20.22.4.16'
  PROBLEM = '2.16.840.1.113883.10.20.22.4.4'
  PROBLEM_STATUS = '2.16.840.1.113883.10.20.22.4.6'
  PROCEDURE = '2.16.840.1.113883.10.20.22.2.7.1'
  VITAL = '2.16.840.1.113883.10.20.22.2.4.1'


class Field(object):
  """A field of a CSV or BigQuery table representation of a CCDA."""

  def __init__(self, name, type='STRING', mode='NULLABLE'):
    self.name = name
    self.type = type
    self.mode = mode

  def to_json(self):
    return {
      'name': self.name,
      'type': self.type,
      'mode': self.mode,
    }


# TODO: Add more fields to the CSV.
CSV_FIELDS = [
    Field('birthplace_city'),
    Field('birthplace_state'),
    Field('birthplace_postal_code'),
    Field('birthplace_country'),
    Field('dob', type='INTEGER'),
    Field('marital_status'),
    Field('gender'),
    Field('race'),
    Field('ethnicity'),
    Field('religion'),
]


class CcdaTree(object):
  """A CCDA document represented as a tree of nodes."""

  def __init__(self, fp):
    self._doc = minidom.parse(fp)

  @classmethod
  def get_code_from_node(cls, node):
    code_val = None  
    code_system_val = None
    name_val = None
    if node:
        code_val =  node.getAttribute('code') 
        if code_val:
           code_system_val = node.getAttribute('codeSystem')
           name_val = node.getAttribute('displayName') 
        else:
           translation_nodes = node.getElementsByTagName('translation') 
           if translation_nodes:
             translation_node = translation_nodes[0]  
             code_val =  translation_node.getAttribute('code') if translation_node else None  
             code_system_val = translation_node.getAttribute('codeSystem') if translation_node else None
             name_val = translation_node.getAttribute('displayName') if translation_node else None
         
    return {
        'code': code_val,
        'code_system': code_system_val,
        'name': name_val,
    }

  def _get_element_by_tag_name(self, tag_name):
    nodes = self._doc.getElementsByTagName(tag_name)
    return nodes[0] if nodes else None

  def _get_code_from_tag_name(self, tag_name):
    node = self._get_element_by_tag_name(tag_name)
    return CcdaTree.get_code_from_node(node)

  def _get_value_of_child_by_tag_name(self, parent_node, tag_name):
    current_node = parent_node.getElementsByTagName(tag_name)  
    if not current_node: 
     return None
    else:
     current_node_val =  current_node[0].firstChild
     if not current_node_val: 
      return None
     else:
      return current_node_val.nodeValue   

  def get_dob(self):
    val = self._get_element_by_tag_name('birthTime').getAttribute('value')
    #return datetime.datetime.strptime(val, '%Y%M%d')
    return self.get_date_from_value(val)

  def get_gender(self):
    return self._get_code_from_tag_name('administrativeGenderCode')

  def get_marital_status(self):
    return self._get_code_from_tag_name('maritalStatusCode')

  def get_language(self):
    return self._get_element_by_tag_name('languageCode').getAttribute('code')

  def get_race(self):
    return self._get_code_from_tag_name('raceCode')

  def get_ethnicity(self):
    return self._get_code_from_tag_name('ethnicGroupCode')

  def get_religion(self):
    return self._get_code_from_tag_name('religiousAffiliationCode')

  def get_birthplace(self):
    node = self._get_element_by_tag_name('birthplace')
    if not node:
      return {
          'city': None,
          'state': None,
          'postal_code': None,
          'country': None,
      }
    addr_node = node.getElementsByTagName('addr')[0]
    _get_val = self._get_value_of_child_by_tag_name
    return {
        'city': _get_val(addr_node, 'city'),
        'state': _get_val(addr_node, 'state'),
        'postal_code': _get_val(addr_node, 'postalCode'),
        'country': _get_val(addr_node, 'country'),
    }

  def get_entries_by_template(self, root, parent=None):
    if parent is None:
      parent = self._doc
    nodes = [
        node.parentNode
        for node in parent.getElementsByTagName('templateId')
        if node.getAttribute('root') == root]
    return nodes

  @classmethod
  def get_date_from_effective_time(cls, entry):
    effectiveTime_nodes =  entry.getElementsByTagName('effectiveTime') 
    returnVal = None
    for effectiveTime_node in effectiveTime_nodes:
      val = effectiveTime_node.getAttribute('value')  if effectiveTime_node else None
      if val is None:
	'''
	When val is None, for e.g.	
		<effectiveTime>
			<low value="20110213"/>
			<high nullFlavor="NA"/>
		</effectiveTime>

	When val is not None, for e.g.
		<effectiveTime value="200003231430"/>
	'''
        low_nodes = effectiveTime_node.getElementsByTagName('low')
        val = low_nodes[0].getAttribute('value') if low_nodes else None    
      returnVal =  cls.get_date_from_value(val)
    return returnVal
    
  @classmethod
  def get_date_from_value(cls, val):
    if val is None:
        return None
    else:
        if len(val) == len('YYYYMMDD'):
          datetime_format = '%Y%m%d'
        elif len(val) == len('YYYYMMDDHHMMSS'):
          datetime_format = '%Y%m%d%H%M%S'
        elif len(val) == len('YYYYMMDDHHMM'):
          datetime_format = '%Y%m%d%H%M'  
        elif len(val) == len('YYYYMMDDHHMMSS-mmmm'):
            if '-' in val:
              datetime_format = '%Y%m%d%H%M%S-%f'  
            elif '+' in val:  
        #elif len(val) == len('YYYYMMDDHHMMSS+mmmm'):
              datetime_format = '%Y%m%d%H%M%S+%f' 
        else:
          return None #      datetime_format = '%Y%m%d%H%M%S' 
      
        return datetime.datetime.strptime(val, datetime_format)

  @classmethod
  def get_date_range_from_node(cls, date_node):
    low_nodes = date_node.getElementsByTagName('low')
    low = low_nodes[0].getAttribute('value') if low_nodes else None
    high_nodes = date_node.getElementsByTagName('high')
    high = high_nodes[0].getAttribute('value') if high_nodes else None
    return {
        'start': cls.get_date_from_value(low) if low else None,
        'end': cls.get_date_from_value(high) if high else None,
    }

  @classmethod
  def get_quantity_message_from_node(cls, node):
    quantity = messages.Quantity()
    quantity.value = node.getAttribute('value')
    quantity.unit = node.getAttribute('unit')
    return quantity
  

class CcdaDocument(object):
  """A CCDA document that can be represented in various ways."""

  def __init__(self, fp):
    self._tree = CcdaTree(fp)

  def to_json(self):
    message = self.to_message()
    #return protojson.MessageJSONEncoder(message.vitals).encode_message()  
    return protojson.encode_message(message)
    #return message.vitals
      
  def to_csv(self):
    """Converts the CCDA document to a CSV file."""
    message = self.to_message()
    row = {
        'birthplace_city': message.demographics.birthplace.city,
        'birthplace_country': message.demographics.birthplace.country,
        'birthplace_postal_code': message.demographics.birthplace.postal_code,
        'birthplace_state': message.demographics.birthplace.state,
        'dob': message.demographics.dob,
        'ethnicity': message.demographics.ethnicity.code,
        'gender': message.demographics.gender.code,
        'marital_status': message.demographics.marital_status.name,
        'race': message.demographics.race.code,
        'religion': message.demographics.ethnicity.code,
    }
    fp = cStringIO.StringIO()
    writer = csv.DictWriter(fp, [field.name for field in CSV_FIELDS])
    writer.writeheader()
    writer.writerow(row)
    fp.seek(0)
    return fp.read()

  def to_message(self):
    """Converts the CCDA document to a ProtoRPC message."""
    # TODO: Remove duplicate code.
    doc = messages.CcdaDocument()
     

    # Demographics.
    doc.demographics = messages.Demographic()
    doc.demographics.dob = self._tree.get_dob()
    doc.demographics.gender = messages.Code(**self._tree.get_gender())
    doc.demographics.marital_status = messages.Code(
        **self._tree.get_marital_status())
    doc.demographics.language = self._tree.get_language()
    doc.demographics.race = messages.Code(
        **self._tree.get_race())
    doc.demographics.ethnicity = messages.Code(
        **self._tree.get_ethnicity())
    doc.demographics.religion = messages.Code(
        **self._tree.get_religion())
    doc.demographics.birthplace = messages.Address(
        **self._tree.get_birthplace())
    
    # Allergies.
    # TODO: Implement allergies.
    doc.allergies = []
    entries = self._tree.get_entries_by_template(Root.ALLERGY)
    for entry in entries:
        allergy = messages.Allergy()
        participantVal = entry.getElementsByTagName('participant')
        
        if participantVal:
            participantRoleVal = participantVal[0].getElementsByTagName('participantRole')
            if participantRoleVal:
                playingEntityVal = participantRoleVal[0].getElementsByTagName('playingEntity')
                if playingEntityVal:
                    codeVals = playingEntityVal[0].getElementsByTagName('code')
                    if codeVals:
                        codeVal = codeVals[0]  
                        allergy.code = messages.Code()
                        allergy.code.code  = codeVal.getAttribute('code')
                        allergy.code.name = codeVal.getAttribute('displayName')
                        allergy.code.code_system = codeVal.getAttribute('codeSystem')
                        allergy.code.code_system_name = codeVal.getAttribute('codeSystemName')
        
        allergyReactionNode = self._tree.get_entries_by_template(Root.ALLERGY_REACTION,entry)   
        
        if allergyReactionNode:
            allergyReactionObservationNode = allergyReactionNode[0]
            if allergyReactionObservationNode:
                valueVals = allergyReactionObservationNode.getElementsByTagName('value')
                if valueVals:
                    valueval = valueVals[0]
                    allergy.reaction = messages.Code()                    
                    allergy.reaction.code  = valueval.getAttribute('code')
                    allergy.reaction.name = valueval.getAttribute('displayName')
                    allergy.reaction.code_system = valueval.getAttribute('codeSystem')
                    allergy.reaction.code_system_name = valueval.getAttribute('codeSystemName')
       
        allergySeverityNode = self._tree.get_entries_by_template(Root.ALLERGY_SEVERITY,entry)   
        
        if allergySeverityNode:
            allergySeverityObservationNode = allergySeverityNode[0]
            if allergySeverityObservationNode:
                valueVals = allergySeverityObservationNode.getElementsByTagName('value')
                if valueVals:
                    valueval = valueVals[0]
                    allergy.severity = messages.Code()                    
                    allergy.severity.code  = valueval.getAttribute('code')
                    allergy.severity.name = valueval.getAttribute('displayName')
                    allergy.severity.code_system = valueval.getAttribute('codeSystem')
                    allergy.severity.code_system_name = valueval.getAttribute('codeSystemName')     
       
        doc.allergies.append(allergy)
        
        
    # Immunizations.
    doc.immunizations = []
    entries = self._tree.get_entries_by_template(Root.IMMUNIZATION)
    for entry in entries:
      product_nodes = self._tree.get_entries_by_template(
          Root.IMMUNIZATION_PRODUCT, parent=entry)
      if product_nodes:
        product_node =  product_nodes[0] 
        immunization = messages.Immunization()
        immunization.date = CcdaTree.get_date_from_effective_time(entry)
        immunization.product = messages.Product()
        code_node = product_node.getElementsByTagName('code')[0]
        product_code = CcdaTree.get_code_from_node(code_node)
        immunization.product.code = messages.Code(**product_code)

        doc.immunizations.append(immunization)

    # Labs.
    doc.labs = []
    lab_parent = self._tree.get_entries_by_template(Root.LAB)
    if lab_parent: 
        entries = lab_parent[0].getElementsByTagName('entry')
        for entry in entries:
          lab = messages.Lab()
          code_node = entry.getElementsByTagName('code')[0]
          lab_code = CcdaTree.get_code_from_node(code_node)
          lab.code = messages.Code(**lab_code)

          lab.results = []
          component_nodes = entry.getElementsByTagName('component')
          for component_node in component_nodes:
            result_code_nodes = component_node.getElementsByTagName('code')
            lab_result = messages.LabResult()
            if result_code_nodes:
              result_code_node = result_code_nodes[0]  
              result_code = CcdaTree.get_code_from_node(result_code_node)              
              lab_result.code = messages.Code(**result_code)

            valueVals = component_node.getElementsByTagName('value')
            if valueVals:
              lab_result.value = valueVals[0].getAttribute('value')
              if lab_result.value:
               lab_result.unit = valueVals[0].getAttribute('unit') 
              else:
                if valueVals[0].firstChild:   
                   lab_result.value = valueVals[0].firstChild.nodeValue
            
            lab_result.date = CcdaTree.get_date_from_effective_time(component_node)
            
            lab.results.append(lab_result)  
          
          doc.labs.append(lab)

      

    # Medications.
    doc.medications = []
    entries = self._tree.get_entries_by_template(Root.MEDICATION)
    for entry in entries:
      medication = messages.Medication()
      medication.product = messages.Product()

      date_node = entry.getElementsByTagName('effectiveTime')[0]
      date_range = CcdaTree.get_date_range_from_node(date_node)
      medication.date_range = messages.DateRange(**date_range)

      product_node = entry.getElementsByTagName('manufacturedProduct')[0]
      product_code_node = product_node.getElementsByTagName('code')[0]
      product_code = CcdaTree.get_code_from_node(product_code_node)
      medication.product.code = messages.Code(**product_code)

      quantity_nodes = entry.getElementsByTagName('doseQuantity')
      if quantity_nodes:
        node = quantity_nodes[0]
        medication.dose_quantity = CcdaTree.get_quantity_message_from_node(node)

      rate_nodes = entry.getElementsByTagName('rateQuantity')
      if rate_nodes:
        node = rate_nodes[0]
        medication.rate_quantity = CcdaTree.get_quantity_message_from_node(node)

      # TODO: precondition, reason, route, vehicle, administration, prescriber.
      doc.medications.append(medication)

    # Problems.
    doc.problems = []
    entries = self._tree.get_entries_by_template(Root.PROBLEM)
    for entry in entries:
      problem = messages.Problem()

      code_node = entry.getElementsByTagName('value')
#      problem_code = CcdaTree.get_code_from_node(code_node)
#      problem.code = messages.Code(**problem_code)
      if code_node:
        valueval = code_node[0]
        problem.code = messages.Code()                    
        problem.code.code  = valueval.getAttribute('code')
        problem.code.name = valueval.getAttribute('displayName')
        problem.code.code_system = valueval.getAttribute('codeSystem')
        problem.code.code_system_name = valueval.getAttribute('codeSystemName') 

      date_nodes = entry.getElementsByTagName('effectiveTime')
      for date_node in date_nodes:
       date_range = CcdaTree.get_date_range_from_node(date_node)
       problem.date_range = messages.DateRange(**date_range)

      status_nodes = self._tree.get_entries_by_template(Root.PROBLEM_STATUS,
                                                       parent=entry)
      if status_nodes:
        status_node = status_nodes[0]
        entry_node = status_node.getElementsByTagName('value')[0]
        problem.status = entry_node.getAttribute('displayName')

      # TODO: Implement problem.age.
      doc.problems.append(problem)

    # Procedures.
    doc.procedures = []
    procedure_parent = self._tree.get_entries_by_template(Root.PROCEDURE)
    if procedure_parent:
        entries = procedure_parent[0].getElementsByTagName('entry')
        for entry in entries:
          procedure = messages.Procedure()
          code_node = entry.getElementsByTagName('code')[0]
          procedure_code = CcdaTree.get_code_from_node(code_node)
          procedure.code = messages.Code(**procedure_code)
          procedure.date = CcdaTree.get_date_from_effective_time(entry)

          # TODO: Implement specimen, performer, device.
          doc.procedures.append(procedure)

    # Vitals.
    doc.vitals = []
    vitals_parent =  self._tree.get_entries_by_template(Root.VITAL)
    if vitals_parent:
        entries = vitals_parent[0].getElementsByTagName('entry')
        for entry in entries:
          vital = messages.Vital()
          vital.date = CcdaTree.get_date_from_effective_time(entry)
          vital.results = []
          result_entries = entry.getElementsByTagName('component')
          for result_entry in result_entries:
            vital_result = messages.VitalResult()
            code_node = result_entry.getElementsByTagName('code')[0]
            value_node = result_entry.getElementsByTagName('value')[0]
            vital_result_code = CcdaTree.get_code_from_node(code_node)
            vital_result.code = messages.Code(**vital_result_code)
            value_attribute = value_node.getAttribute('value')
            if value_attribute:
                #if not value_attribute.isalnum():
                try:
                    vital_result.value = long(float(value_attribute))
                except ValueError:
                    vital_result.value = None
            else:
                vital_result.value = None
            vital_result.unit = value_node.getAttribute('unit')
            vital.results.append(vital_result)
          doc.vitals.append(vital)

    return doc
