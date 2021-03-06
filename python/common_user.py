import os

user_file_path = "/home/sujan/Documents/read2lead/horizon/horizon_users/"
 

def read_file(file):
	users = []
	with open(file, 'r') as f:
		users = f.readlines()
		#print(f.readlines())
	return [user.strip() for user in users if len(user) > 2]

def get_total_user_count(all_users):
	unique_users = []
	for pool, users in all_users:
		unique_users += users

	with open("/home/sujan/Desktop/report.txt", 'a') as f:
		for user in set(unique_users):
			f.write(user+"\n")

	return len(set(unique_users)), set(unique_users)


def get_user_associated_pool(total_users, all_users):
	user_pools = []
	for user in total_users:
		pools = []
		for pool, users in all_users:
			if user in users:
				pools.append(pool)
		user_pools.append([user, pools])
	return (user_pools)


def display_result(user_pools):
	one_pool_user = 0
	two_pool_user = 0
	three_pool_user = 0
	four_pool_user = 0
	f2 = open('users_in_multiple_pool.txt', 'a')
	f = open('user_associated_pool.txt','a')

	print("\n##########################################\n")
	for user, pool in user_pools:
		if len(pool) == 1:
			print(user , pool)
			f.write("\n" + user + " " + str(pool))
			one_pool_user += 1
	f.write("\n\n")

	print("\n##########################################\n")
	print("Total one Pool User :", one_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")
	for user, pool in user_pools:
		if len(pool) == 2:
			print(user, pool)
			f.write("\n" + user + " " + str(pool))
			f2.write("\n" + user + " " + str(pool))
			two_pool_user += 1

	f.write("\n\n")

	print("\n##########################################\n")
	print("Total two Pool User :", two_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")

	for user, pool in user_pools:
		if len(pool) == 3:
			print(user, pool)
			f.write("\n" + user + " " + str(pool))
			f2.write("\n" + user + " " + str(pool))
			three_pool_user += 1

	f.write("\n\n")


	print("\n##########################################\n")
	print("Total three Pool User :", three_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")

	for user, pool in user_pools:
		if len(pool) == 4:
			print(user, pool)
			f.write("\n" + user + " " + str(pool))
			f2.write("\n" + user + " " + str(pool))
			four_pool_user += 1
	f.write("\n\n")


	print("\n##########################################\n")
	print("Total four Pool User :", four_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")



def inactive_users_associated_pools(inactive_users_file, user_pools_file):
	#find pools associated with inactive for more than 30 days:
	#read inactive users list
	#find pools from the user_pools list
	inactive_users = []
	user_pools = []
	inactive_user_pools = []
	with open(inactive_user_pools, 'r') as f:
		inactive_users = r.readlines()

	with open(user_pools_file, 'r') as f:
		user_pools = r.readlines()

	for inactive_user in inactive_users:
		print(inactive_users)



def notify_if_multiple_pool_assigned():
	
	pass


def get_report(all_users):
	#total horizon users
	#users with multiple pool asssigned
	#users active 
	#users inactive


	total_horizon_users, all_horizon_users = get_total_user_count(all_users)
	print(total_horizon_users, all_horizon_users)
	
	user_pools = get_user_associated_pool(all_horizon_users, all_users)

	#write user associated pool in file:

	display_result(user_pools)


# def read_file(user_file_path):
# 	all_users = []
# 	for file in os.listdir(user_file_path):
# 		all_users.append([file, read_file(user_file_path+file)])

# 	get_report(all_users)


if __name__ == "__main__":
	#read_file(user_file_path)

	inactive_user_file = "inactive_user_for_30_days.txt"
	user_pool_file = "user_associated_pool.txt"
	inactive_users_associated_pools(inactive_users_file, )

	all_users = []
	for file in os.listdir(user_file_path):
		if "Desktop" in file:
			all_users.append([file, read_file(user_file_path+file)])
	

	get_report(all_users)