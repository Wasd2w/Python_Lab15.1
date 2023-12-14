import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо CSV файл
file_path = 'comptagevelo20152.csv'
df = pd.read_csv(file_path)

# Перетворюємо стовпець 'Date' у тип datetime
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Встановлюємо 'Date' як індекс
df.set_index('Date', inplace=True)

# Вибираємо тільки числові стовпці
numeric_columns = df.select_dtypes(include='number')

# Групуєємо та агрегуємо за місяцем
monthly_sum = numeric_columns.resample('M').sum()

# Знаходимо місяць з найбільшою сумою
most_popular_month = monthly_sum.sum(axis=1).idxmax().strftime('%B')

print(f"Найбільш популярний місяць серед велосипедистів: {most_popular_month}")

# Видаляємо час з індексів
monthly_sum.index = monthly_sum.index.strftime('%Y-%m')

# Побудова графіку
plt.figure(figsize=(10, 6))
monthly_sum.sum(axis=1).plot(kind='bar', color='skyblue')
plt.title('Сумарне використання велодоріжок за місяць')
plt.xlabel('Місяць')
plt.ylabel('Сума використання')
plt.show()
