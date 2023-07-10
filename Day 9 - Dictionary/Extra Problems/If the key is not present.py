# If the key is not present

country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}
 
try:
    print(country_code['India'])
    print(country_code['USA'])
except KeyError:
    print('Not Found')