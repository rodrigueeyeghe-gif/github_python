## exo_8.1##############################
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f)

## exo_8.2##############################
print(e2f['walrus'])

## exo_8.3##############################
f2e = {x:y for y, x in e2f.items()}
print(f2e)

## exo_8.4##############################
print(f2e['chien'])

## exo_8.5##############################
print(e2f.keys())
print(list(e2f.keys()))

## exo_8.6##############################
life = {
    'animals':
            {"cats":["Henri", "Grumpy", "Lucy"],
             "octopi":{},
             "emus":{}
             },
              'plants':{},
              'other':{}
            }
print(life)

## exo_8.7##############################
print(life.keys())

## exo_8.8##############################
print(life['animals'].keys())

## exo_8.9##############################
print(life['animals']['cats'])

## exo_8.10##############################
squares = {x : x*x  for x in range(10) }
print(squares)

## exo_8.11##############################
odd = {x for x in range(10) if x%2 == 1}
print(odd)

## exo_8.12##############################
for x in ('Got %s' % number for number in range(10)):
    print(x)

## exo_8.13##############################
    
    
