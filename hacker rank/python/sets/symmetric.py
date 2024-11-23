raw_input()
english = set( raw_input().split() )
raw_input()
french = set( raw_input().split() )

english = english ^ french
print len(english)
