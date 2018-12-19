import data_basa
import permanent

basa = data_basa.Basa()
'''
basa.create_tables()
basa.add_admin('Slava', '2604')
basa.add_admin('Oksana', '1005')
basa.add_admin('Karim', '1111')

basa.add_open_user('user1', 1, '0001')
basa.add_open_user('user2', 1, '0002')
basa.add_open_user('user3', 2, '0003')
basa.add_open_user('user4', 3, '0004')
basa.add_open_user('user5', 4, '0005')
basa.add_open_user('user6', 4, '0006')

basa.add_close_user(1, '1001')
basa.add_close_user(1, '1002')
basa.add_close_user(2, '1003')
basa.add_close_user(3, '1004')
basa.add_close_user(4, '1005')
basa.add_close_user(4, '1006')
'''
#print(basa.get_user_by_role(1))
#print(basa.get_role_by_OKo('0006'))
#print(basa.get_user_by_OKo('0006'))
#basa.change_role('0005', 1)
#basa.change_role('0006', -1)
#basa.go_out_IK('0004')
#basa.go_to_IK('0003')
#basa.delete_user('0005')
#basa.not_to_be_auditor('0004')
#basa.change_personal_data('0001', '46513', 'sgdgdgrd')
#print(basa.get_OKo_by_user('Karim'))
#basa.create_open_voting('0003', '0003', 16, 4, 2018, 2)
#question = ['what to do?', 'huyarit', 'bejat']
#basa.create_close_voting(1, question, 16, 4, 2018, 3)

"""
basa.add_open_user('user8', 4, '0008')
basa.add_open_user('user9', 3, '0009')
basa.add_open_user('user10', 3, '0010')
"""

#basa.calculate_open_decision(1)
#print(basa.get_roles())
#basa.calculate_close_decision(2)
#basa.make_close_choice(2, '0001', 1)
#print(basa.get_active_close_voting('1003'))
# print(basa.get_user_by_OKo('0000'))
print(basa.get_OKo_by_user('Slava'))