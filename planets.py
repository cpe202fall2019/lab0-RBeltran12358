def weight_on_planets():
   weight = input("What do you weigh on earth? ")
   e_weight = float(weight)

   m_weight = .38 * e_weight
   j_weight = 2.34 * e_weight

   tuple = ('\nOn Mars you would weigh', m_weight,"pounds.\nOn Jupiter you would weigh", j_weight, "pounds.")

   print(tuple[0],tuple[1],tuple[2],tuple[3],tuple[4])

if __name__ == '__main__':
   weight_on_planets()

