def avgInList(list):
   total = 0
   if (len(list) == 0):
      return 0
   for i in range(0, len(list)):
      total += list[i]

   return total / len(list)
