# DB
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

# Functions

def create_item_table():
	c.execute('CREATE TABLE IF NOT EXISTS itemstable(category TEXT,subcategory TEXT,name TEXT,price INTEGER,discount INTEGER, quantity INTEGER,likes INTEGER,isnew TEXT,brand TEXT,colour1 TEXT,colour2 TEXT,photo TEXT)')

def add_item_data(category,subcategory,name,price,discount,quantity,likes,isnew,brand,colour1,colour2,photo):
	c.execute('INSERT INTO itemstable(category,subcategory,name,price,discount,quantity,likes,isnew,brand,colour1,colour2,photo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
		   (category,subcategory,name,price,discount,quantity,likes,isnew,brand,colour1,colour2,photo))
	conn.commit()

def view_all_inventry_items():
	c.execute('SELECT * FROM itemstable')
	data = c.fetchall()
	return data

def view_unique_item():
    c.execute('SELECT DISTINCT name FROM itemstable')
    data = c.fetchall()
    return data

def get_item(name):
    c.execute('SELECT * FROM itemstable WHERE name = "{}" '.format(name))
    data = c.fetchall()
    return data

def edit_item(newitem_category,newitem_sub_category,newitem_name,newitem_price,newitem_discount,newitem_quantity,newitem_isnew,newitem_brand,
			  newitem_color_varient_1,newitem_color_varient_2,newitem_image,get_category,get_subcategory,get_name,get_price,
			  get_discount,get_isnew,get_brand,get_colour1,get_colour2,get_url):
    c.execute('UPDATE itemstable SET category=?,subcategory=?,name=?,price=?,discount=?,quantity=?,likes=0,isnew=?,brand=?,colour1=?,colour2=?,photo=?  WHERE category=? AND subcategory=? and name=? AND price=? AND discount=? AND likes=0 AND isnew=? AND brand=? AND colour1=? AND colour2=? and photo=?',
			  (newitem_category,newitem_sub_category,newitem_name,newitem_price,newitem_discount,newitem_quantity,newitem_isnew,newitem_brand,
			  newitem_color_varient_1,newitem_color_varient_2,newitem_image,get_category,get_subcategory,get_name,get_price,
			  get_discount,get_isnew,get_brand,get_colour1,get_colour2,get_url))
    conn.commit()
    data = c.fetchall()
    return data

def delete_item(name):
	c.execute('DELETE FROM itemstable WHERE name="{}"'.format(name))
	conn.commit()


# Login/Signup



def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable (name TEXT, age INTEGER, gender TEXT, username TEXT PRIMARY KEY, password TEXT,usertype TEXT)')


def add_userdata(name,age,gender,username,password,usertype):
	c.execute('INSERT INTO userstable(name,age,gender,username,password,usertype) VALUES (?,?,?,?,?,?)',
		   (name,age,gender,username,password,usertype))
	conn.commit()
	

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def get_user_type(username):
    c.execute('SELECT usertype FROM userstable WHERE username = ?', (username,))
    user_type = c.fetchone()
    if user_type:
        return user_type[0]
    else:
        return None
	
#Inventory functions 
def get_item_by_name(item_name):
    c.execute("SELECT * FROM itemstable WHERE name = ?", (item_name,))
    item = c.fetchone()
    if item:
        return {
            'category': item[0],
            'subcategory': item[1],
            'name': item[2],
            'price': item[3],
            'discount': item[4],
            'quantity': item[5],
            'likes': item[6],
            'isnew': item[7],
            'brand': item[8],
            'colour1': item[9],
            'colour2': item[10],
            'photo': item[11]
        }
    else:
        return None

def update_item_quantity(item_name, updated_quantity):
    try:
        c.execute("UPDATE itemstable SET quantity = ? WHERE name = ?", (updated_quantity, item_name))
        conn.commit()
        print(f"Successfully updated quantity for {item_name}")
    except sqlite3.Error as e:
        print(f"Error updating quantity for {item_name}: {str(e)}")
