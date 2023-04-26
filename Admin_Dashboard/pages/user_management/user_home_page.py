import time
from pathlib import Path

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path


class UserHomePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.seleniumdriver = SeleniumDriver(self.driver)

    # locators
    _download_bulk_csv = "//button[normalize-space()='Download csv']"

    _groups_field = "//input[@placeholder='Group']"
    # _edit_english_user_btn = "//tbody/tr[2]/td[6]/button[1]"
    _edit_any_one_user_btn = "//button[@class='btn btn-primary btn-sm btn-icon']"
    # _edit_box_first_name_field = "//input[@id='mat-input-8']"
    # _edit_box_first_name_field = "//input[@id='mat-input-0']" # xpath
    # _edit_box_first_name_field = "mat-input-0"  # id
    _edit_box_first_name_field = '//input[@name="first-name"]'  # xpath
    _save_updated_uder = "//button[normalize-space()='Save']"

    # delete users
    _click_delete_icon = '//button[@class="btn btn-danger btn-sm btn-icon"]'
    _pop_up_choose_delete_user = "//button[normalize-space()='Delete user']"

    def download_bulk_csv_btn(self):
        self.elementClick(self._download_bulk_csv, locatorType="xpath")
        self.waitForElement(locator=self._download_bulk_csv, locatorType="xpath")
        self.seleniumdriver.screen_shot(file="test_3_2_4_bulk_user_csv_download")

    # def verify_download(self):
    #     # specify the directory path where the files are located
    #     filepath = os.path.join(str(Path.home() / "Downloads"))
    #     print(f"filepath-{filepath}")
    #
    #     # specify the starting words of the file name you want to select
    #     starts_with = "users_"
    #
    #     # list all files in the directory
    #     files = os.listdir(filepath)
    #
    #     # iterate over the files and select the ones that start with the specified words
    #     selected_files = [file for file in files if file.startswith(starts_with)]
    #
    #     # print the selected files
    #     print(selected_files)

    def verify_download(self):
        # specify the directory path where the files are located
        filepath = os.path.join(os.getcwd(), "Downloaded_Files")
        print(f"filepath-{filepath}")

        # specify the starting words of the file name you want to select
        starts_with = "users_"

        # list all files in the directory
        files = os.listdir(filepath)

        # iterate over the files and select the ones that start with the specified words
        selected_files = [file for file in files if file.startswith(starts_with)]

        # print the selected files
        print(selected_files)

    def delete_file(self):
        downloaded_dir = os.path.join(os.getcwd(), "Downloaded_Files")
        print(downloaded_dir)
        for f in os.listdir(downloaded_dir):
            print(f)
            file_name = os.path.join(downloaded_dir, f)
            try:
                if os.path.exists(file_name):
                    os.remove(file_name)
                print(f"{f} is deleted successfully.")
            except:
                print(f"File {f} not found")

    def filter_grp(self, grp_name):
        self.sendKeys(grp_name, self._groups_field, locatorType="xpath")
        self.hold_wait()

    def edit_user_btn(self):
        # self.elementClick(self._edit_english_user_btn, locatorType="xpath")
        self.elementClick(self._edit_any_one_user_btn, locatorType="xpath")

    def clear_fileds(self):
        first_name = self.getElement(locator=self._edit_box_first_name_field, locatorType="xpath")
        first_name.clear()
        self.hold_wait()

    def first_name_new_data(self, first_name_new):
        self.backspace_clear(self._edit_box_first_name_field, locatorType="xpath")
        self.sendKeys(first_name_new, self._edit_box_first_name_field, locatorType="xpath")
        self.hold_wait()

    def save(self):
        self.elementClick(self._save_updated_uder, locatorType="xpath")

    _cancel_btn_xpath = "//button[normalize-space()='Cancel']"

    def cancel(self):
        self.elementClick(self._cancel_btn_xpath, locatorType="xpath")

    def edit_user(self, first_name_new):
        # if user found then only
        self.edit_user_btn()
        # self.clear_fileds()
        self.backspace_clear(self._groups_field, locatorType="xpath")
        self.first_name_new_data(first_name_new)
        self.seleniumdriver.screen_shot(file="test_3_2_6_edit_user")
        self.save()
        self.hold_wait()

    _click_out = "//body"

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")

    _select_groups_dropdown = "//ns-filter-select[@label='Groups']"
    _unselect_n_groups = "//span[@class='mat-option-text' and contains(text(), 'Automation_Test_Group')]"
    _error_msg_xpath = "//mat-error[contains(text(), ' At least one group should be selected.')]"

    def edit_user_remove_grp_name(self):
        self.backspace_clear(self._groups_field, locatorType="xpath")
        self.edit_user_btn()
        self.hold_wait()
        self.elementClick(self._select_groups_dropdown, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._unselect_n_groups, locatorType="xpath")
        time.sleep(3)
        # self.click_out()

        error_available = self.isElementPresent(self._error_msg_xpath, locatorType="xpath")
        if error_available:
            print("error message available")
        else:
            print("error message not available")
        self.seleniumdriver.screen_shot(file="test_3_2_6_1_edit_user_unselect_grp")
        self.hold_wait()
        # self.double_clicks(self._cancel_btn_xpath, locatorType="xpath")
        self.hold_wait()

    _select_extra_groups = "//span[@class='mat-option-text' and contains(text(), 'Admin-Automation_Test_Customer')]"
    _list_box = "//div[@role='listbox']"
    _all_grps = "//mat-option[@role='option']"

    def select_multiple_grps(self):
        self.refresh_page()
        self.filter_grp("Automation_Test_Group")
        # self.backspace_clear(self._groups_field, locatorType="xpath")
        "Automation_Test_Group is already selected, we will add one more"
        self.edit_user_btn()
        self.hold_wait()
        self.elementClick(self._select_groups_dropdown, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_extra_groups, locatorType="xpath")
        self.hold_wait()

        "verify that user has mutiple grp selected"
        self.edit_user_btn()
        self.hold_wait()
        self.elementClick(self._select_groups_dropdown, locatorType="xpath")
        self.hold_wait()
        all_grps = self.getElements(self._all_grps, locatorType="xpath")
        print(f"lenth: {len(all_grps)}")
        n = 0
        for grp in all_grps:
            get_attribute = grp.get_attribute("aria-selected")
            if get_attribute == "true":
                n += 1
        print(f"number of groups selected: {n}")
        self.seleniumdriver.screen_shot(file="test_3_2_6_2_edit_user_select_mutliple_grp")

        """
        below code is only to click on SAVE button, due to GROUP pop-up is open, it is not able to click SAVE directly
        without below double click
        """
        self.double_clicks(self._save_updated_uder, locatorType="xpath")  # this is save element
        self.hold_wait()
        self.hold_wait()
        # self.save()
        self.hold_wait()

    _first_name_first_occurance = "//table//tr[1]//td[2]"

    def verify_rename(self):
        time.sleep(1)
        get_value = self.getElement(self._first_name_first_occurance, locatorType="xpath")
        rename_value = get_value.text
        return rename_value

    def click_bin_icon(self):
        self.elementClick(self._click_delete_icon, locatorType="xpath")

    def choose_delete_btn(self):
        self.elementClick(self._pop_up_choose_delete_user, locatorType="xpath")

    _number_users = "//tbody[@role='rowgroup']//tr"
    _page_size_click = "//div[@id='mat-select-value-1']"
    _page_size_set = "//span[@class='mat-option-text'][normalize-space()='50']"

    def delete_user(self):
        self.move_to_element(self._page_size_set, locatorType="xpath")
        self.elementClick(self._page_size_set, locatorType="xpath")
        self.hold_wait()
        self.move_to_element(self._groups_field, locatorType="xpath")
        self.hold_wait()

        self.filter_grp("Automation_Test_Group")
        self.hold_wait()
        counte = []
        counte = self.getElements(self._number_users, locatorType="xpath")
        for cou in counte:
            print(cou)
            print(f"Number of Users: {len(counte)}")

        i = 0
        while i < len(counte):
            self.backspace_clear(self._groups_field, locatorType="xpath")
            self.filter_grp("Automation_Test_Group")
            self.hold_wait()
            self.click_bin_icon()
            self.choose_delete_btn()
            self.hold_wait()
            i += 1

    _find_range = "//div[@class='paginator-range-label']"

    def del_user_new(self):
        self.backspace_clear(self._groups_field, locatorType="xpath")
        self.filter_grp("Automation_Test_Group")

        self.move_to_element(self._find_range, locatorType="xpath")
        number_of_users_xpath = self.getElement(self._find_range, locatorType="xpath")
        number_of_users_text = number_of_users_xpath.text
        if number_of_users_text == "0 of 0":
            str_number_of_users = number_of_users_text.split(" ")[2]
            int_number_of_users = int(str_number_of_users)
            print(f"----number_of_users: {number_of_users_text}")
            print(f"----str_number_of_users: {str_number_of_users}")
            print(f"----int_number_of_users: {int_number_of_users}")
            print(type(int_number_of_users))
        else:
            str_number_of_users = number_of_users_text.split(" ")[4]
            int_number_of_users = int(str_number_of_users)
            print(f"----number_of_users: {number_of_users_text}")
            print(f"----str_number_of_users: {str_number_of_users}")
            print(f"----int_number_of_users: {int_number_of_users}")
            print(type(int_number_of_users))

        # while int_number_of_users > 0:
        #     self.move_to_element(self._groups_field, locatorType="xpath")
        #     self.backspace_clear(self._groups_field, locatorType="xpath")
        #     self.filter_grp("Automation_Test_Group")
        #     self.hold_wait()
        #     self.click_bin_icon()
        #     self.choose_delete_btn()
        #     self.hold_wait()
        #     int_number_of_users -= 1

        if int_number_of_users > 0:
            for i in range(int_number_of_users + 1):
                self.move_to_element(self._groups_field, locatorType="xpath")
                self.backspace_clear(self._groups_field, locatorType="xpath")
                self.filter_grp("Automation_Test_Group")
                self.hold_wait()
                self.click_bin_icon()
                self.choose_delete_btn()
                # self.hold_wait()
                # time.sleep(0.40)
                # return self.verify_deletes()

                # time.sleep(2)
        else:
            print("No existing users are available")

    _snackbar_xpath = "//span[contains(text(),'deleted!')]"

    def verify_deletes(self):
        snackbar_element = self.getElement(self._snackbar_xpath, locatorType="xpath")
        snackbar_text = snackbar_element.text
        # print(f" this user is deleted: {snackbar_text}")
        # cut string
        # start = snackbar_text[:4]  # select the first 04 Char
        end = snackbar_text[-8:]
        # print(f"end is :{end}")

        # return snackbar_text.find("deleted!")
        return end
