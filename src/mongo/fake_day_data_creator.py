from datetime import timedelta

num_of_years = 5

def create_days_array(start_date, end_date):
  date_array = []
  current_date = start_date
  
  while current_date <= end_date:
    date_str = current_date.strftime('%d/%m/%Y')
    day_of_week = current_date.weekday()  # Monday is 0 and Sunday is 6
    
    date_array.append({
      'date_id': 'date_id_' + date_str,
      'date': current_date,
      'day_of_week': ((day_of_week + 1) % 7) + 1
    })
    
    current_date += timedelta(days=1)
  
  return date_array
