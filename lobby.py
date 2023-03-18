from identification import go_online, go_offline, set_username
from find_user import find_online_users
from game import game_server, game_client


def online_users():
  global users
  users = {}

  for i in find_online_users():
    users[i['username']] = i['ip_address']

  return users


def main():

  # connecting to the network
  username = input('Enter username: ')
  while username in online_users():
    username = input('Username already taken.\nEnter username: ')
  set_username(username)

    # sample menu program
  while True:

    # print online users
    print('---online users---')
    for user in online_users():
      print(user)

    # get input
    user_input = input('--MENU--\n(1) Go Online (wait for incoming connections)\n(2) Play against an Online Player\n(3) Refresh\n-->')
    while user_input != '1' and user_input != '2' and user_input != '3':
      print('WRONG INPUT')

    if user_input == '1':
      go_online()
      print('waiting for incoming connection')
      game_server()
      go_offline()
    
    elif user_input == '2':
      chosen_opponent = input('Enter opponent username: ')
      users = online_users()
      while chosen_opponent not in users:
         chosen_opponent = input('No such user online.\nEnter opponent username: ')
         users = online_users()

      chosen_opponent_ip = users[chosen_opponent]  
      game_client(chosen_opponent_ip)

    elif user_input == '3':
        # next iteration will print the new online users
      continue

    else:
      print('Invalid Input!')
  
if __name__ == '__main__':
  main()