import random

categories_data = [
  {
    'name': 'Coffee',
    'hebrewNeme': 'קפה',
    'basePrice': 10,
    'types': [
      {
        'name': 'Espresso',
        'hebrewNeme': 'אספרסו',
      },
      {
        'name': 'Cappuccino',
        'hebrewNeme': 'קפוצינו',
      },
      {
        'name': 'Latte',
        'hebrewNeme': 'לאטה',
      },
      {
        'name': 'Americano',
        'hebrewNeme': 'אמריקנו',
      },
      {
        'name': 'Macchiato',
        'hebrewNeme': 'מקיאטו',
      },
      {
        'name': 'Mocha',
        'hebrewNeme': 'מוקה',
      },
    ],
  },
  {
    'name': 'Ice_Cream',
    'hebrewNeme': 'גלידה',
    'basePrice': 18,
    'types': [
      {
        'name': 'Vanilla',
        'hebrewNeme': 'וניל',
      },
      {
        'name': 'Chocolate',
        'hebrewNeme': 'שוקולד',
      },
      {
        'name': 'Strawberry',
        'hebrewNeme': 'תות',
      },
      {
        'name': 'Cookie_Dough',
        'hebrewNeme': 'בצק עוגיות',
      },
      {
        'name': 'Mint_Chocolate_Chip',
        'hebrewNeme': 'שוקולד ציפס ומנטה',
      },
      {
        'name': 'Cookies_and_Cream',
        'hebrewNeme': 'קצפת עוגיות',
      },
      {
        'name': 'Pistachio',
        'hebrewNeme': 'פיסטוק',
      },
    ],
  },
  {
    'name': 'Cans',
    'hebrewNeme': 'פחיות',
    'basePrice': 7,
    'types': [
      {
        'name': 'Coca_Cola',
        'hebrewNeme': 'קוקה קולה',
      },
      {
        'name': 'Coca_Cola_Zero',
        'hebrewNeme': 'קוקה קולה זירו',
      },
      {
        'name': 'Fanta',
        'hebrewNeme': 'פנטה',
      },
      {
        'name': 'Sprite',
        'hebrewNeme': 'ספרייט',
      },
      {
        'name': '7UP',
        'hebrewNeme': '7 אפ',
      },
    ],
  },
  {
    'name': 'Beer',
    'hebrewNeme': 'בירה',
    'basePrice': 28,
    'types': [
      {
        'name': 'Heineken',
        'hebrewNeme': 'הייניקן',
      },
      {
        'name': 'Carlsberg',
        'hebrewNeme': 'קרלסברג',
      },
      {
        'name': 'Corona',
        'hebrewNeme': 'קורונה',
      },
    ],
  },
]

def create_products_array():
  products_array = []

  for category in categories_data:    
    for product in category['types']:
      random_number_add_to_price = random.randint(0, round(category['basePrice'] * 0.3))
      random_number_sub_for_cost = random.randint(round(category['basePrice'] * 0.4), round(category['basePrice'] * 0.7))
      
      products_array.append({
        'product_id': category['name'] + '_' + product['name'],
        'category': category['name'],
        'categoryHebrewNeme': category['hebrewNeme'],
        'name': product['name'],
        'hebrewNeme': product['hebrewNeme'],
        'price': category['basePrice'] + random_number_add_to_price,
        'cost': category['basePrice'] - random_number_sub_for_cost,
      })

  return products_array
