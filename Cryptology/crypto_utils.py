## Crypto utilities

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
eng_alph_probs = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002, .008, .040, .024, .067, .075, .019, .001, .060, .063, .091, .028, .010, .023, .001, .020, .001]


def let_to_num(letter):
  return alphabet.index(letter)


def num_to_let(number):
  return alphabet[number%26]
  
  
def xor(str1, str2):
    b_out = []
    for b1,b2 in zip(str1, str2):
        if b1=='0':
            if b2=='0':
                b_out.append('0')
            else:
                b_out.append('1')
        else: # b1 is 1
            if b2=='0':
                b_out.append('1')
            else: 
                b_out.append('0')
    return b_out
	

def index_of_coincidence(text):
  i_of_c = 0
  N = len(text)
  for i in range(26):
    num = text.count(alphabet[i])
    num = float(num*(num-1))
    denom = N*(N-1)
    i_of_c += float(num/denom)
  return i_of_c
	
  
# to break Vignere cipher
def calc_ys(k, text):
  y1 = ""
  y2 = ""
  y3 = ""
  y4 = ""
  y5 = ""
  y6 = ""
  y7 = ""
  for index in range(len(text)):
    if index % k == 0:
      y1 += text[index]
    elif index % k == 1:
      y2 += text[index]
    elif index % k == 2:
      y3 += text[index]
    elif index % k == 3:
      y4 += text[index]
    elif index % k == 4:
      y5 += text[index]
    elif index % k == 5:
      y6 += text[index]
    elif index % k == 6:
      y7 += text[index]

  return [y1,y2,y3,y4,y5,y6,y7]
  

# modified for stream Vignere cipher
def calc_ys_mod(k, text):
  y1 = ""
  y2 = ""
  y3 = ""
  y4 = ""
  y5 = ""
  y6 = ""
  y7 = ""
  for index in range(len(text)):
    shift = index//k # how many rotations have happened
    val = num_to_let(let_to_num(text[index])-shift)
    if index % k == 0:
      y1 += val
      # print("here" +text[index])
      # print(num_to_let(let_to_num(text[index])-shift))
    elif index % k == 1:
      y2 += val
    elif index % k == 2:
      y3 += val
    elif index % k == 3:
      y4 += val
    elif index % k == 4:
      y5 += val
    elif index % k == 5:
      y6 += val
    elif index % k == 6:
      y7 += val

  return [y1,y2,y3,y4,y5,y6,y7]
  

# merge table for determining keyword in Vignere
def calc_M(text):
  N = len(text)
  Mg = [0]*len(eng_alph_probs)

  for k in range(26): # for each shift k calculate M(g)
    for i in range(26):
      f_alpha = text.count(alphabet[(i+k)%26])/N
      p_alpha = eng_alph_probs[i]
      Mg[k] += f_alpha*p_alpha

    Mg[k] = str(round(Mg[k], 3))

  print('A-G: ' + ' '.join(Mg[0:7]))
  print('H-N: ' + ' '.join(Mg[7:14]))
  print('O-U: ' + ' '.join(Mg[14:21]))
  print('V-Z: ' + ' '.join(Mg[21:26]))