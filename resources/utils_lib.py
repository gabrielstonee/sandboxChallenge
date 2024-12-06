
def get_window_handles(driver):
    """
    Get Current Window handles available

    :param driver: reference to our driver instance
    """
    window_handles = driver.window_handles
    return window_handles

def switch_window(driver, current_window):
    """
    Switch to a new window

    :param driver: reference to our driver instance
    """
    window_handles = get_window_handles(driver)
    for handle in window_handles:
        if handle != current_window:
            driver.switch_to.window(handle)
            break

def check_elements_from_invoice_list(expected_dict, actual_list):
    """
    Validate if the the elements of the Invoice Details List is accordingly to the values expected

    :param expected_list: list with the expected values
    :param actual_list: list with the actual values
    """
    incorrect_elements = []
    dict_keys = list(expected_dict.keys())
    
    for index, key in enumerate(dict_keys):
        if str(expected_dict[key]) != str(actual_list[index]):
            incorrect_elements.append(key)
    
    return incorrect_elements
    