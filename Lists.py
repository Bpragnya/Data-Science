import sys
import logging


class Lists:
    """
    Class of basic list operations using Exception handling and logging
    """
    default_list = [1, 11, 23, 2, 08.45, 99, 67, 78.45]
    logging.basicConfig(filename="test_log_file.log", format='%(name)s - %(levelname)s - %(asctime)s - %(message)s',
                        level=logging.DEBUG)
    logging.info("From class Lists")

    # open_list2 = [23, 45, 99]
    # open_list3 = [[3, 8, 56, 9, 2]]

    # constructor
    def __init__(self_ptr):
        pass
        # print("Default list is: ", self_ptr.default_list)

    def add_value(its_ptr, value):
        """
        list operation function to add elements in the list
        :param value:
        :return: None
        """
        try:
            logging.debug("user value for append is " + value)
            its_ptr.default_list.append(int(value))
            print("your value ", value, " added successfully")
            logging.debug("user value " + value + " added successfully")
            print("consolidated list is:", its_ptr.default_list)
            logging.debug("consolidated list is:" + str(its_ptr.default_list))
        except Exception as e:
            logging.exception("Exception '"+ str(e)+ "' raised while appending value "+ value+ " in the list ",
                              str(its_ptr.default_list))

    def add_value_at_pos(its_ptr, value, pos):
        """
        List operation function to add element at the position in the list
        :param value:
        :param pos:
        :return: None
        """
        try:
            its_ptr.default_list.insert(int(pos), int(value))
            print("your value ", value, " is added at position ", pos, " successfully")
            logging.debug("user value "+ value+ " is added at position "+ pos+ " successfully")
            print("consolidated list is:", its_ptr.default_list)
            logging.debug("consolidated list is:"+ str(its_ptr.default_list))
        except Exception as e:
            logging.exception("Exception '"+ str(e)+ "' raised while inserting value "+ value+ ' at position '+ pos+
                              ' in the list '+ str(its_ptr.default_list))

    def rem_value(its_ptr, value):
        """
        Function to remove value from the list
        :param value:
        :return: None
        """
        try:
            its_ptr.default_list.remove( int(value))
            print("your value ", value, " is removed successfully")
            logging.debug("user value "+ value+ " is removed successfully")
            print("consolidated list after removing value is:", its_ptr.default_list)
            logging.debug("consolidated list after removing value is:"+ str(its_ptr.default_list))
        except Exception as e:
            logging.exception("Exception '"+ str(e)+ "' raised while removing value "+ value+ ' from the list '+ str(its_ptr.default_list))

    def rem_lst_element(its_ptr):
        """
        Function to remove last element from the list
        :return:
        """
        try:
            rem_ele = its_ptr.default_list.pop()
            print("removed last element ", rem_ele, " successfully")
            logging.debug("removed last element "+ str(rem_ele)+ " successfully")
            print("consolidated list after removing value is:", its_ptr.default_list)
            logging.debug("consolidated list after removing value is:"+ str(its_ptr.default_list))
        except Exception as e:
            logging.exception("Exception '"+ str(e)+ "' raised while pop operation from the list "+ str(its_ptr.default_list))

    def rv_lst(its_ptr):
        """
        Function to reverse list
        :return: None
        """
        try:
            its_ptr.default_list.reverse()
            print("reversed list is:", its_ptr.default_list)
            logging.debug("reversed list is:"+ str(its_ptr.default_list))
        except Exception as e:
            logging.exception("Exception '"+ str(e)+ "' raised while reversing the list "+ str(its_ptr.default_list))

    def sort_lst(its_ptr, is_reverse):
        """
        Function to sort list in ASC or DESC order
        :param is_reverse:
        :return:
        """
        try:
            its_ptr.default_list.sort(reverse=is_reverse)
            print("sorted list values are :", its_ptr.default_list)
            logging.debug("sorted list values are :"+ str(its_ptr.default_list))
        except Exception as e:
            order = 'desc' if is_reverse==True else 'asc'
            logging.exception("Exception '"+ str(e)+ "' raised while sorting the list "+ str(its_ptr.default_list)+ ' in order '+
                              order)

    def count_no_of_occurance(its_ptr, value):
        """
        Function to count no of occurrences of the value given
        :param value:
        :return: None
        """
        try:
            no_of_occ = its_ptr.default_list.count(int(value))
            print("no of occurrence of ", value, " in the list is :", no_of_occ)
            logging.debug("no of occurrence of "+ value+ " in the list is :"+ str(no_of_occ))
        except Exception as e:
            logging.exception("Exception '"+ str(e)+ "' raised while counting the no of occurrence of value "+ value+
                              ' in the list '+str(its_ptr.default_list))

    def ind_of(its_ptr, value):
        """
        Function to find index of first occurrence of the given value
        :param value:
        :return: None
        """
        try:
            ind = its_ptr.default_list.index(int(value))
            print("index of first occurance of ", value, " from the list is :", ind)
            logging.debug("index of first occurance of "+ value+ " from the list is :"+ str(ind))
        except Exception as e:
            logging.exception("Exception '"+ str(e)+ "' raised while finding index of value "+ value+ ' in the list '+
                              str(its_ptr.default_list))


while True:
    try:
        list_var = Lists()
        print("""Hi, you can perform following list operations in this class:
        1) add your element(s) in the list
        2) add element at position in the list
        3) remove value from the list
        4) remove last element from the list
        5) sort list 
        6) reverse list
        7) count no of occurrence of value in the list 
        8) find the index of first occurrence of value in the list
        9) Exit
        
        default list in this class is :""", list_var.default_list)
        u_choice = int(input("Enter your choice: "))
        logging.info("user input is :"+ str(u_choice))
        if u_choice == 1:
            list_var.add_value(input("Enter your value:"))
        if u_choice == 2:
            pos = input("Enter position :")
            list_var.add_value_at_pos(input("Enter your value:"), pos)
        if u_choice == 3:
            print("Existing default list is ", list_var.default_list)
            list_var.rem_value(input("Enter the value from list:"))
        if u_choice == 4:
            list_var.rem_lst_element()
        if u_choice == 5:
            while True:
                order_by = input("Order by asc or desc?")
                if order_by.lower() == 'asc':
                    is_reverse = False
                    break
                elif order_by.lower() == 'desc':
                    is_reverse = True
                    break
                else:
                    logging.warning("user input value for order by is improper :"+ order_by.lower())
            list_var.sort_lst(is_reverse)
        if u_choice == 6:
            list_var.rv_lst()
        if u_choice == 7:
            while True:
                # print("Existing default list is ", list_var.default_list)
                u_inp = input("Enter your value from the list:")
                if int(u_inp) in list_var.default_list:
                    break
            list_var.count_no_of_occurance(u_inp)
        if u_choice == 8:
            while True:
                u_inp = input("Enter your value from the list:")
                if int(u_inp) in list_var.default_list:
                    break
            list_var.ind_of(u_inp)
        if u_choice == 9:
            print("Thank you")
            break;
    except:
        a, b, c = sys.exc_info()
        logging.exception("exception class"+ str(a))
        logging.exception("exception message"+ str(b))
        logging.exception("line number"+ str(c.tb_lineno))
