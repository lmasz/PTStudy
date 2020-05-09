## Crypto utilities

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
eng_alph_probs = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002, .008, .040, .024, .067, .075, .019, .001, .060, .063, .091, .028, .010, .023, .001, .020, .001]


def mod_inverse(x, n):
    # returns x_inv st x*xinv (mod n) = 1
    for i in range(n):
        if (x*i) % n == 1:
            return i
        
        
def fastModExp(b, e, n):  # Fast modular exponentiation e.g.: y = b^e mod n
    # From Hannah
    if (n == 1):
        y = 0;
        return
    
    y = 1
    b = b % n
    while ( e > 0 ):
        if (e % 2 == 1):
            y = (y*b) % n  # mod((y * b),n)
            e = e >> 1  #bitshift(e,-1)
            b = (b**2) % n
            
    return y
    

def rsa_encrypt(m, e, N): # c = m^e mod N 
    post_exp = m**e
    post_mod = post_exp % N
    return post_mod
    
    
# ModExp(a,k,n)
def ModExp(a,k,n, debug):
    k = str(bin(k))  # put it in binary
    k_vals = k.split('b')
    k_vals = k_vals[1]
    b = 1
    A = a
    t = len(k_vals)
    if k_vals[-1]=='1':
        b = a
    i = 1
    while i < t:
        A = A**2 % n
        if k[-1-i] == '1':
            b = (A*b) % n
        if debug:
            print("i= " +str(i)+", a= " +str(A)+ ", b= " +str(b))
        i += 1
    return b


def gcd(m, n):
    gcd = 1
    larger = m
    if n > m:
        larger = n
    for i in range(1, larger+1):
        if m % i == 0 and n % i == 0: # i is a factor of m and n
            gcd = i
    return gcd


# Then compute the exponent a from phi(n)
# 1 < d < φ(N) and ed ≡ 1 mod φ(N)
def compute_phi(n):
    phi_of_n = []
    for i in range(1, n):
        gcd_val = gcd(i, n)
        if gcd_val == 1:
            phi_of_n.append(i)
    return phi_of_n


def factor(n: int):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
            
    return factors


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
    

def word_2_base26ish(word):
    total = 0
    d = len(word)
    for i in range(d):
        total = total + (let_to_num(word[i])*(26**(d-i-1)))
        
    return total
# This is the wrong way, ...

# now reverse it
def base26ish_2_word(value):
    total = 0
    word = ['','','']
    for i in range(2,-1,-1):
        letter = value // (26**i)
        word[2-i] = (num_to_let(letter))
        value = value - (letter*(26**i))
        
    return word

