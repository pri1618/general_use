import random

avalM = {'a1': '1', 'a2': '2', 'a3': '3', 'b1': '4', 'b2': '5', 'b3': '6', 'c1': '7', 'c2': '8', 'c3': '9'}
moved = {}

while True:
  sym = str(raw_input('Glyph of choice(o/x): '))
  if sym == 'o':
    compSym = 'x'
    break
  elif sym == 'x':
    compSym = 'o'
    break
  else:
    print('Invalid Input.')

print('\n')

while True:
  order_p = str(raw_input('r - random. u - user plays first. c - computer plays first.\nYour Input: '))
  if order_p == 'r':
    orders = ['u', 'c']
    order_p = random.choice(orders)
    break
  elif order_p == 'u' or order_p == 'c':
    break
  else: 
    print('Invalid Input.')          

map = '___|___|___\n___|___|___\n   |   |   '
map_l = list(map)

print('\n')
print(map)
print('\n')

counter = 0

def check(symbol):
  l3 = []
  l4 = []
  
  for x, y in moved.items():
    l3.append(x[0]+y)
    l4.append(x[1]+y)
 
  if l3.count('a' + symbol) == 3 or l3.count('b' + symbol) == 3 or l3.count('c' + symbol) == 3 or l4.count('1' + symbol) == 3 or l4.count('2' + symbol) == 3 or l4.count('3' + symbol) == 3:
    return True
  
  elif 'b2' in moved.keys() and moved['b2'] == symbol:
    if (('a1' in moved.keys() and moved['a1'] == symbol) and ('c3' in moved.keys() and moved['c3'] == symbol)) or (('a3' in moved.keys() and moved['a3'] == symbol)and('c1' in moved.keys() and moved['c1'] == symbol)):
      return True     

def short(coord, symbol):
  l5 = []
  l6 = []
  l7 = []
  l8 = ['1', '2', '3']
  lx = []
  for i in list(moved.keys()):
    if moved[i] == symbol:
      l5.append(i[0])
      l6.append(i[1])
  l7.append(l6[l5.index(coord)])
  l6.pop(l5.index(coord))
  l5.pop(l5.index(coord))
  l7.append(l6[l5.index(coord)])
  for i in l8:
    if i not in l7:
      lx.append(i)
  move_i = coord+lx[0]
  return move_i


def short_1(coord, symbol):
  move_i = ''
  l5 = []
  l6 = []
  l7 = []
  l9 = ['a', 'b', 'c']
  lx = []
  for i in list(moved.keys()):
    if moved[i] == symbol:
      l5.append(i[0])
      l6.append(i[1])
  l7.append(l5[l6.index(coord)])
  l5.pop(l6.index(coord))
  l6.pop(l6.index(coord))
  l7.append(l5[l6.index(coord)])
  for i in l9:
    if i not in l7:
      lx.append(i)
  move_i = lx[0]+coord
  return move_i


def brain():
  l5 = []
  l6 = []
  l0 = []
  ly = []
  ly5 = []
  ly6 = []
  lt = ['a1', 'c3', 'a3', 'c1'] 
  ls = ['a2', 'c2', 'b1', 'b3']
  for i in list(moved.keys()):
    if moved[i] == sym:
      l5.append(i[0])
      l6.append(i[1])
      l0.append(i)
    else:
      ly.append(i)
      ly5.append(i[0])
      ly6.append(i[1])  
  
  if counter == 1 or counter == 0:
    if 'b2' not in l0:
      return 'b2'
    else:
      return list(avalM.keys())[random.randrange(0, len(avalM))]           

  elif ly5.count('a') == 2 and short('a', compSym) in avalM:
      return short('a', compSym)
      
  elif ly5.count('b') == 2 and short('b', compSym) in avalM:
    return short('b', compSym)        
     
  elif ly5.count('c') == 2 and short('c', compSym) in avalM:
    return short('c', compSym)

  elif ly6.count('1') == 2 and short_1('1', compSym) in avalM:
    return short_1('1', compSym)

  elif ly6.count('2') == 2 and short_1('2', compSym) in avalM:
    return short_1('2', compSym)

  elif ly6.count('3') == 2 and short_1('3', compSym) in avalM:
    return short_1('3', compSym)
        
  elif 'b2' in ly and (('a1' in ly and 'c3' in avalM) or ('a3' in ly and 'c1' in avalM) or ('c1' in ly and 'a3' in avalM) or ('c3' in ly and 'a1' in avalM)):
    if 'a1' in ly and 'c3' in avalM:
      return 'c3'
    elif 'a3' in ly and 'c1' in avalM:
      return 'c1'
    elif 'c3' in ly and 'a1' in avalM:
      return 'a1'
    elif 'c1' in ly and 'a3' in avalM:
      return 'a3'

  elif (('a1' in l0 and 'c3' in l0) or ('a3' in l0 and 'c1' in l0)) and 'b2' in avalM:
    return 'b2'

  elif counter == 2:   
    if l0[0] in lt:
      for i in range(len(lt)):
        if lt[i] == l0[0]:
          if l0[0][0] == 'a':
            return lt[i+1]
          else:
            return lt[i-1]
    else:
      for i in lt:
        if i in avalM:
          return i          
  
  else:                 #Block
    if l5.count('a') == 2 and short('a', sym) in avalM:
      return short('a', sym)
    
    elif l5.count('b') == 2 and short('b', sym) in avalM:
      return short('b', sym)        
    
    elif l5.count('c') == 2 and short('c', sym) in avalM:
      return short('c', sym)

    elif l6.count('1') == 2 and short_1('1', sym) in avalM:
      return short_1('1', sym)

    elif l6.count('2') == 2 and short_1('2', sym) in avalM:
      return short_1('2', sym)

    elif l6.count('3') == 2 and short_1('3', sym) in avalM:
      return short_1('3', sym)

    elif 'b2' in l0 and (('a1' in l0 and 'c3' in avalM) or ('a3' in l0 and 'c1' in avalM) or ('c1' in l0 and 'a3' in avalM) or ('c3' in l0 and 'a1' in avalM)):
      if 'a1' in l0:
        return 'c3'
      elif 'a3' in l0:
        return 'c1'
      elif 'c3' in l0:
        return 'a1'
      elif 'c1' in l0:
        return 'a3'

    elif (('a1' in l0 and 'c3' in l0) or ('a3' in l0 and 'c1' in l0)) and 'b2' in list(avalM.keys()):
      return 'b2'
    
    elif counter == 4:  
      for i in lt:
        if i in avalM and (l5.count(i[0]) == 0 or l6.count(i[1]) == 0):
          return i

    else:
      return list(avalM.keys())[random.randrange(0, len(avalM))]


def play(symbol, move_p):
  brd = '_1_|_2_|_3_\n_4_|_5_|_6_\n 7 | 8 | 9 '
  brd_l = list(brd)
  
  index = brd_l.index(avalM[move_p])
  map_l[index] = symbol

  return map_l


def big_play(player):
  if player == 'c':
    move = brain()
    symbol_i = compSym
  else:
    while True:
      move = str(raw_input('Your Move: '))
      if move not in avalM:
        print('Invalid Input/Square Taken')
      else:
        break
    symbol_i = sym
  
  board = play(symbol_i, move)
  print(''.join(board) + '\n') 
  
  move_log = {move: symbol_i} 
  moved.update(move_log) 
  avalM.pop(move)
    
x = ''

while True:
  if order_p == 'c':
    big_play('c')
    counter += 1

    if check(compSym) == True:
      x = 'c_win'
      break

    if counter == 9: break
    
    big_play('u')
    counter += 1

    if check(sym) == True:
      x = 'u_win'
      break

  else:
    big_play('u')
    counter += 1

    if check(sym) == True:
      x = 'u_win'
      break

    if counter == 9: break 

    big_play('c')
    counter += 1

    if check(compSym) == True:
      x = 'c_win'
      break

if x == 'u_win':
  print('You Won!')
elif x == 'c_win':
  print('You Lost.')
else:
  print('Draw.')    

  
