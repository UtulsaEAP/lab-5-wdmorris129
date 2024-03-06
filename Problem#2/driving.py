def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   cost = miles_driven / miles_per_gallon * dollars_per_gallon
   return cost

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

if __name__ == '__main__':
   print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
   print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):.2f}')