# membuat kamus
fc_barcelona = {
    'UCL' : '5',
    'Liga' : '29',
    'CDR' : '36',
    'Super' : '32'
}

print(fc_barcelona['UCL'])
print(fc_barcelona['Liga'])
print(fc_barcelona['CDR'])
print(fc_barcelona['Super'])

# mengubah/menambah
fc_barcelona['Piala Dunia'] = '5'
fc_barcelona['CDR'] = '30'

print(fc_barcelona['CDR'])
print(fc_barcelona['Piala Dunia'])

for key in fc_barcelona:
    print(key)