import pyodbc as odbc # pip install pypyodbc
import pandas as pd # pip install pandas

# Import CSV
data = pd.read_csv (r'C:\Users\souro\Desktop\DOT Project\2018_Yellow_Taxi_Trip_Data.csv')   
df = pd.DataFrame(data)

# Connect to SQL Server
conn = odbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QP7FKES;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE YellowTaxi (
			VendorID int,
			tpep_pickup_datetime datetime,
			tpep_dropoff_datetime datetime,
            passenger_count int,
            trip_distance decimal(18,0),
            RatecodeID nchar(10),
            store_and_fwd_flag char(10),
            PULocationID int,
            DOLocationID int,
            payment_type int,
            fare_amount decimal(18,0),
            extra decimal(18,0),
            mta_tax decimal(18,0),
            tip_amount decimal(18,0),
            tolls_amount decimal(18,0),
            improvement_surcharge decimal(18,0),
            total_amount decimal(18,0)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO YellowTaxi (VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, RatecodeID, store_and_fwd_flag, PULocationID, DOLocationID, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.VendorID,
                row.tpep_pickup_datetime,
                row.tpep_dropoff_datetime,
                row.passenger_count,
                row.trip_distance,
                row.RatecodeID,
                row.store_and_fwd_flag,
                row.PULocationID,
                row.DOLocationID,
                row.payment_type,
                row.fare_amount,
                row.extra,
                row.mta_tax,
                row.tip_amount,
                row.tolls_amount,
                row.improvement_surcharge,
                row.total_amount
                )
conn.commit()