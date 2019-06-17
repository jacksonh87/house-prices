#- * -coding: utf - 8 - * -
    
"""
Created on Mon Jun 17 19: 28: 27 2019

@author: jacks

See https: //www.gov.uk/guidance/about-the-price-paid-data#explanations-of-column-headers-in-the-ppd

Data item                           Explanation(where appropriate)
Transaction unique identifier:      A reference number which is generated
                                    automatically recording each published sale.
                                    The number is unique and will change each
                                    time a sale is recorded.
Price:                              Sale price stated on the transfer deed.
Date of Transfer:                   Date when the sale was completed, as stated
                                    on the transfer deed.
Postcode:                           This is the postcode used at the time of the
                                    original transaction. Note that postcodes
                                    can be reallocated and these changes are not
                                    reflected in the Price Paid Dataset.
Property Type:                      D = Detached, S = Semi - Detached,
                                    T = Terraced, F = Flats / Maisonettes,
                                    O = Other
Old / New:                          Indicates the age of the property and
                                    applies to all price paid transactions,
                                    residential and non - residential.
                                    Y = a newly built property,
                                    N = an established residential building
Duration Relates to the tenure:     F = Freehold, L = Leasehold etc.
PAON:                               Primary Addressable Object Name.
                                    Typically the house number or name.
SAON:                               Secondary Addressable Object Name.
                                    Where a property has been divided into
                                    separate units(for example, flats), the
                                    PAON(above) will identify the building and
                                    a SAON will be specified that identifies the
                                    separate unit / flat.
Street
Locality
Town / City
District
County
PPD Category Type:                  Indicates the type of Price Paid transaction.
                                    A = Standard Price Paid entry, includes
                                    single residential property sold for full
                                    market value.
                                    B = Additional Price Paid entry including
                                    transfers under a power of sale /
                                    repossessions, buy - to - lets(where they
                                    can be identified by a Mortgage) and
                                    transfers to non - private individuals.
Record Status - monthly file only   Indicates additions, changes and deletions
                                    to the records.(see guide below).
                                    A = Addition
                                    C = Change
                                    D = Delete.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_london = pd.read_csv('ppd_data_LON.csv', header = None)
data_kent = pd.read_csv('ppd_data_KENT.csv', header = None)
data = pd.concat([data_kent, data_london])

data.columns = ['transaction_id', 'price', 'date', 'postcode', 'property_type',
    'new_build', 'tenure', 'house_number', 'flat_number', 'street', 'locality',
    'city', 'district', 'county', 'ppd_type', 'record_status'
]

districts = ['NEWHAM', 'LAMBETH', 'LEWISHAM', 'BEXLEY', 'BROMLEY', 'CROYDON',
    'TOWER HAMLETS', 'GREENWICH', 'SEVENOAKS', 'DARTFORD'
]
lower_price = 200000
upper_price = 300000
data = data[data.district.isin(districts)]
data = data[(data.price >= lower_price) & (data.price <= upper_price)]
# data = data[(data.property_type == 'D') | (data.property_type == 'S')]
# data = data[(data.tenure == 'F')]
data = data[data.postcode.notnull()]
split_postcode = [i.split(' ') for i in data.postcode]
data['left'] = [i[0] for i in split_postcode]
data['right'] = [i[1] for i in split_postcode]

plt.hist(data.price, bins = 20)

print(data.district.value_counts())
# data = data[data.left == 'E16']
