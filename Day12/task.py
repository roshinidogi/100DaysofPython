enemies = 1
def inc_enemies():
# We can use 'global' and get the global variable and modify it in function
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")
inc_enemies()
# we can do it without changing the global variable
def inc_enemies(enemy):
    enemy += 1
    print(f"enemies inside function: {enemy}")
    return enemy
inc_enemies(enemies)
# # print(f"enemies outside function: {enemies}")
# #Local Scope
# def drink_portion():
#     portion = 2
#     print(portion)
# drink_portion()
# # print(portion) won't work bcz it's out of scope
# #Global Scope
# portion_health = 10
# def drink_health():
#     print(portion_health)
# drink_health()
# Global constants are normally declared in upper case
PI = 3.14
GOOGLE_URL = "www.google.com"

