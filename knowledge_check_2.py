import pandas as pd

animal_in_out = pd.read_csv('Louisville_Metro_KY_-_Animal_Service_Intake_and_Outcome.csv')
#fixing column names to snake case
print(animal_in_out.columns)
animal_in_out = animal_in_out.rename(
    columns={'animalid' : 'animal_id',
             'intype' : 'in_type',
             'insubtype' : 'in_subtype',
             'indate' : 'in_date',
             'surreason' : "surrender_reason",
             'outtype' : 'out_type',
             'outsubtype' : 'out_subtype',
             'outdate' : 'out_date',
             'animaltype' : 'animal_type',
             'petsize' : 'pet_size',
             'sourcezipcode' : 'souce_zip_code'}
)

print(animal_in_out.columns)

#replaing NaN values with 'None'
print(animal_in_out['out_subtype'][2])
animal_in_out = animal_in_out.fillna('None')
print(animal_in_out['out_subtype'][2])
