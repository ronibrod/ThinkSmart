categories_data = [
  {
    'name': 'Coffee',
    'hebrewNeme': 'קפה',
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
      products_array.append({
        'product_id': category['name'] + '_' + product['name'],
        'category': category['name'],
        'categoryHebrewNeme': category['hebrewNeme'],
        'name': product['name'],
        'hebrewNeme': product['hebrewNeme'],
      })

  return products_array
