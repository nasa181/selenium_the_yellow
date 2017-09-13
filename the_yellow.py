from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import numpy as np


proxy_index = 0
list_free_proxy = [
					
				]
proxy_index_length = len(list_free_proxy)


list_red_key = [
					['MAZD10BH','MAZD14AF','MAZD16BS'],
					['MAZD10BL','MAZD14AL','MAZD16CF'],
					[],
					['AUDI14AM','AUDI16AA'],
					['HOND10AE','HOND14AA','HOND16CJ'],
					['NISS14AK','NISS16AW'],
					['TOYO10EH','TOYO14BA','TOYO16BV'],
					['HOND16CI'],
					['MERC14BT','MERC16DF'],
					['TOYO10AA','TOYO14AV','TOYO16CE'],
					['HOND10AY','HOND14BE','HOND16CO'],
					['HOND10BD','HOND14BM','HOND16AK'],
					['MAZD16AL'],
					['MAZD14AQ','MAZD16AM'],
					['ISUZ10AL','ISUZ14CY','ISUZ16CE'],
					['TOYO10BL','TOYO14EU','TOYO16BF'],
					['TOYO16AD'],
					['HOND14CY','HOND16CA'],
					['HOND10AL','HOND14BK','HOND16BH'],
					['MITS10AG','MITS14AO','MITS16AF']
				]

list_car_brand = ['Mazda','Mazda','BMW','Audi','Honda','Nissan','Toyota','Honda','Mercedes-Benz','Toyota','Honda','Honda','Mazda','Mazda','Isuzu','Toyota','Toyota','Honda','Honda','Mitsubishi']
list_car_model = ['2','3','320d','A3','Accord','Almera','Corolla Altis','BR-V','C300','Camry','Civic','CR-V','CX-3','CX-5','D-Max','Fortuner','Hilux Revo','HR-V','Jazz','Pajero Sport']
# there is no information for BMW
list_car_desc = [
					['1.5i 4doors Groove Auto 4speed - THB 240000','1.5i 4doors Elegance Groove Auto 4speed - THB 300000','1.3i 4doors High Auto 6speed - THB 450000'],
					['1.6i 4doors Groove Auto 4speed,?Imported - THB 280000','1.6i 4doors Groove Auto 4speed - THB 370000','2.0i 4doors C SA Auto 6speed - THB 680000'],
					[],
					['1.4Ti 4doors Limousine SA Auto 7speed Imported (TFSI) - THB 1200000','1.4Ti 4doors Limousine SA Auto 7speed Imported (TFSI) - THB 1300000'],
					['2.0i 4doors E i-VTEC SA Auto 5speed - THB 510000','2.0i 4doors EL i-VTEC SA Auto 5speed - THB 820000','2.0i 4doors E i-VTEC SA Auto 5speed - THB 1000000'],
					['1.2i 4doors E Auto 4speed - THB 280000','1.2i 4doors E Auto speed - THB 340000'],
					['1.6i 4doors Altis CNG Man 5speed - THB 290000','1.6i 4doors Altis E Auto 4speed (CNG) - THB 420000','1.6i 4doors E Auto 7speed (CNG) - THB 780000'],
					['1.5i 4doors SV Auto speed - THB 630000'],
					['2.1DTTi 4doors Blue TEC HYBRID AMG Dynamic G-Tronic Plus Auto 7speed Imported - THB 2200000','2.0Ti 2doors AMG Dynamic G-Tronic Plus Auto 9speed Imported - THB 3500000'],
					['2.0i 4doors E Auto 4speed - THB 460000','2.0i 4doors G Extremo SA Auto 4speed - THB 810000','2.0i 4doors G Extremo SA Auto 6speed - THB 1150000'],
					['1.8i 4doors E i-VTEC SA Auto 5speed (ABS/Airbag SRS with Leather seats) - THB 410000','1.5i 4doors Hybrid CVT speed - THB 570000','1.5i 4doors Turbo CVT speed - THB 840000'],
					['2.0i 4doors E SA Auto 5speed 4WD (ABS/Airbag SRS with Leather seats) - THB 510000','2.0i 4doors E SA Auto 5speed 4WD - THB 770000','2.0i 4doors E SA Auto 5speed 4WD - THB 960000'],
					['1.5DTi 4doors XDL SA Auto 6speed - THB 840000'],
					['2.0i 4doors C Auto 6speed FWD,Imported - THB 760000','2.0i 4doors C Auto 6speed FWD,Imported - THB 860000'],
					['2.5DCT 2doors Ext Cab Hi-Lander Super Platinum Man 5speed RWD - THB 420000','2.5DCT 2doors Ext Cab Hi-Lander L Man 5speed RWD - THB 500000','1.9DCT 2doors Ext Cab Hi-Lander L Man 6speed RWD - THB 560000'],
					['2.5DCT 4doors G Man 5speed RWD - THB 530000','2.5DCT 4doors G Man 5speed RWD - THB 740000','2.4DCT 4doors G Man 6speed RWD - THB 910000'],
					['2.4DCT 2doors Single Cab J Man 5speed RWD - THB 420000'],
					['1.8i 4doors E Auto speed - THB 700000','1.8i 4doors E Auto speed - THB 750000'],
					['1.5i 4doors S i-VTEC Auto 5speed - THB 340000','1.3i 4doors Hybrid Auto speed - THB 430000','1.5i 4doors S i-VTEC Auto 5speed - THB 460000'],
					['2.5DCT 4doors GLS Auto 4speed RWD - THB 490000','2.4i 4doors GLS Man 5speed RWD - THB 580000','2.4DCT 4doors GLS LTD Auto 5speed RWD - THB 860000']
				]

list_car_make_year = np.array([
						['2010','2014','2016'],
						['2010','2014','2016'],
						['2010','2014','2016'],# leave this loop blank (no information)
						['2014','2016'], 
						['2010','2014','2016'],
						['2014','2016'],
						['2010','2014','2016'],
						['2016'],
						['2014','2016'],
						['2010','2014','2016'],
						['2010','2014','2016'],
						['2010','2014','2016'],
						['2016'],
						['2014','2016'],
						['2010','2014','2016'],
						['2010','2014','2016'],
						['2016'],
						['2014','2016'],
						['2010','2014','2016'],
						['2010','2014','2016']
					])
sleep_time = 1.5 # second
list_cm_sex = ['M','F']
list_cm_age = ['35','45','55']
list_cm_birth_year = ['1982 (2525)','1972 (2515)','1962 (2505)']
birth_date = '1'
birth_month = 'ม.ค.'
cm_name='Aj DVD'
cm_phone='0888888888'
cm_email='test@test.com'
currentPolicyNumber = '1010101010'
find_elem_time = 0.1 #second


for i in range(19,len(list_car_brand)):
	for j in range(len(list_car_make_year[i])):
		for k in range(len(list_cm_sex)):
			for x in range(len(list_cm_birth_year)):
				if len(list_car_desc[i])==0:
					print('skip loop')
					garage_str = ',' + list_car_brand[i] + ',' + list_car_model[i] + ',' + list_car_make_year[i][j] + ',' + 'GARAGE' + ',' + list_cm_age[x] + ',' + list_cm_sex[k] + ',' + 'DirectAsia' + ',' + 'no info\n'
					# dealer_str = ',' + list_car_brand[i] + ',' + list_car_model[i] + ',' + list_car_make_year[i][j] + ',' + 'DEALER' + ',' + list_cm_age[x] + ',' + list_cm_sex[k] + ',' + 'DirectAsia' + ',' + 'no info\n'
					f = open('directAsia_version2_data.csv','a')
					f.write(garage_str)
					# f.write(dealer_str)
					f.close()
					print(garage_str)
					# print(dealer_str)
					continue
				find_thing = ''
				chrome_options = ''
				driver = ''
				while len(find_thing) == 0:	
					chrome_options = webdriver.ChromeOptions()
					chrome_options.add_argument('--proxy-server=%s' % list_free_proxy[proxy_index])
					driver = webdriver.Chrome(chrome_options=chrome_options)
					driver.get("https://hide.me/en/check")
					find_thing = driver.find_elements_by_partial_link_text('Check again')
					if len(find_thing) == 0:
						driver.close()
						print(list_free_proxy[proxy_index])
					proxy_index = (proxy_index + 1)%proxy_index_length
				driver.get("http://www.directasia.co.th/")
				elem = driver.find_element(By.XPATH, '//a[@href="/get-car-insurance-quote-form/"]')
				elem.click()
				time.sleep(sleep_time)


				wait = WebDriverWait(driver, 30) # wait 30 second
				# ===============================================
				# 
				# 		///////////  car detail ///////////
				# 
				# ===============================================
				make_year = ''
				while len(make_year) == 0:
					make_year = driver.find_elements(By.XPATH, '//select[@id="vehicleFirstReg"]')
					print('finding car make year')
					time.sleep(find_elem_time)
				make_year_option = ''
				while len(make_year_option) == 0:
					make_year_option = driver.find_elements(By.XPATH, '//select[@id="vehicleFirstReg"]/option[contains(text(),"' + list_car_make_year[i][j] +'")]')
					time.sleep(find_elem_time)
					print('finding' + list_car_make_year[i][j])
				select = Select(driver.find_element(By.XPATH, '//select[@id="vehicleFirstReg"]'))
				select.select_by_visible_text(list_car_make_year[i][j])
				time.sleep(sleep_time)


				try:
					wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//select[@id="vehicleMake"]')))
				except:
					print('waiting fail at car brand')
				car_brand = ''
				while len(car_brand) == 0:
					car_brand = driver.find_elements(By.XPATH, '//select[@id="vehicleMake"]')
					time.sleep(find_elem_time)
					print('finding car brand')
				car_brand_option = ''
				while len(car_brand_option) == 0:
					car_brand_option = driver.find_elements(By.XPATH, '//select[@id="vehicleMake"]/option[contains(text(),"' + list_car_brand[i] +'")]')
					time.sleep(find_elem_time)
					print('finding' + list_car_brand[i])
				time.sleep(sleep_time)
				select = Select(driver.find_element(By.XPATH, '//select[@id="vehicleMake"]'))
				select.select_by_visible_text(list_car_brand[i])
				time.sleep(sleep_time)


				veh_model = ''
				while len(veh_model) == 0:
					veh_model = driver.find_elements(By.XPATH, '//select[@id="vehicleModel"]')
					time.sleep(find_elem_time)
					print('finding car model')
				veh_model_option = ''
				while len(veh_model_option) == 0:
					veh_model_option = driver.find_elements(By.XPATH, '//select[@id="vehicleModel"]/option[contains(text(),"' + list_car_model[i] +'")]')
					time.sleep(find_elem_time)
					print('finding' + list_car_model[i])
				select = Select(driver.find_element(By.XPATH, '//select[@id="vehicleModel"]'))
				select.select_by_visible_text(list_car_model[i])
				time.sleep(sleep_time)


				veh_desc = ''
				while len(veh_desc) == 0:
					veh_desc = driver.find_elements(By.XPATH, '//select[@id="vehicleDesc"]')
					time.sleep(find_elem_time)
					print('finding car desc')
				veh_desc_option = ''
				while len(veh_desc_option) == 0:
					veh_desc_option = driver.find_elements(By.XPATH, '//select[@id="vehicleDesc"]/option[contains(text(),"' + list_car_desc[i][j] +'")]')
					time.sleep(find_elem_time)
					print('finding' + list_car_desc[i][j])
				select = Select(driver.find_element(By.XPATH, '//select[@id="vehicleDesc"]'))
				select.select_by_visible_text(list_car_desc[i][j])
				time.sleep(sleep_time)

				# ========================================================
				# 
				# 		///////////  main driver detail ///////////
				# 
				# ========================================================

				try:
					wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//select[@id="mainDriverDOBDD"]')))
				except:
					print('waiting fail at birth date')
				birth_date_button = ''
				while len(birth_date_button) == 0:
					birth_date_button = driver.find_elements(By.XPATH, '//select[@id="mainDriverDOBDD"]')
					time.sleep(find_elem_time)
					print('finding birth date button')
				birth_date_option = ''
				while len(birth_date_option) == 0:
					birth_date_option = driver.find_elements(By.XPATH, '//select[@id="mainDriverDOBDD"]/option[contains(text(),"' + birth_date +'")]')
					time.sleep(find_elem_time)
					print('finding birth date option')
				time.sleep(sleep_time)
				select = Select(driver.find_element(By.XPATH, '//select[@id="mainDriverDOBDD"]'))
				select.select_by_visible_text(birth_date)
				time.sleep(sleep_time)


				try:
					wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//select[@id="mainDriverDOBMON"]')))
				except:
					print('waiting fail at birth month')
				time.sleep(sleep_time)
				birth_month_button = ''
				while len(birth_month_button) == 0:
					birth_month_button = driver.find_elements(By.XPATH, '//select[@id="mainDriverDOBMON"]')
					time.sleep(find_elem_time)
					print('finding birth month button')
				birth_month_option = ''
				while len(birth_month_option) == 0:
					birth_month_option = driver.find_elements(By.XPATH, '//select[@id="mainDriverDOBMON"]/option[contains(text(),"' + birth_month +'")]')
					time.sleep(find_elem_time)
					print('finding birth month option')
				select = Select(driver.find_element(By.XPATH, '//select[@id="mainDriverDOBMON"]'))
				select.select_by_visible_text(birth_month)
				time.sleep(sleep_time)


				try:
					wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//select[@id="mainDriverDOBYear"]')))
				except:
					print('waiting fail at birth year')
				birth_year_button = ''
				while len(birth_year_button) == 0:
					birth_year_button = driver.find_elements(By.XPATH, '//select[@id="mainDriverDOBYear"]')
					time.sleep(find_elem_time)
					print('finding birth year button')
				# birth_year_option = ''
				# while len(birth_year_option) == 0:
				# 	birth_year_option = driver.find_elements(By.XPATH, '//select[@id="mainDriverDOBYear"]/option[contains(text(),"' + list_cm_birth_year[x] +'")]')
				# 	time.sleep(find_elem_time)
				# 	print('finding ' + list_cm_birth_year[x])
				time.sleep(sleep_time)
				select = Select(driver.find_element(By.XPATH, '//select[@id="mainDriverDOBYear"]'))
				select.select_by_visible_text(list_cm_birth_year[x])
				time.sleep(sleep_time)


				genders = driver.find_elements(By.XPATH, '//button[@data-ng-click="mainDriver.GenderId = i.key;dLCE(6,mainDriver.GenderId); validations.checkDOBEmpty();"]')
				if list_cm_sex[k] == 'M':
					genders[0].click()
				else:
					genders[1].click()
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//button[@data-ng-click="mainDriver.MaritalStatusId = i.key;dLCE(7,mainDriver.MaritalStatusId); validations.checkDOBEmpty();"]')
				elem.click()
				time.sleep(sleep_time)
				

				driver.execute_script("window.scrollTo(0, 650);") # scroll down a bit
				usage = driver.find_elements(By.XPATH, '//button[@data-ng-click="asset.InDriveWork = i.key; onBtnInDriveWorkChange();dLCE(8,asset.InDriveWork); validations.checkDOBEmpty();"]')
				if len(usage) > 0:
					usage[1].click()
					time.sleep(sleep_time)

				
				elem = driver.find_element(By.XPATH, '//button[@data-ng-clicks="onBtnCalculatePremiumClicked(policyHolder.Identifier, frmAboutYou.nricPolicyholder)"]')
				elem.click()
				time.sleep(sleep_time)

				
# ===============================================================================================================================================================================
# 
# 				////////// page: selecting coverage(selecting type)
# 
# ===============================================================================================================================================================================
				
				# ========================================================
				# 
				# 		///////////  ins type V1 ///////////
				# 
				# ========================================================

				ins_type = ''
				while len(ins_type) == 0:
					ins_type = driver.find_elements(By.XPATH, '''//button[@ng-click="selectCoverage(c); dLCE(10,c.Name);"]''')
					time.sleep(find_elem_time)
					print('finding V1')
				ins_type[0].click()
				time.sleep(sleep_time)

# ======================== sum ins V1 =======================
				sum_ins_V1 = driver.find_elements(By.XPATH, '''//span[@data-ng-if="sumInsured.visible"]/span[@data-ng-class="{'da-override-font-size1': HKLocale.getLocale() === 'th-th'}"]''')
				print(len(sum_ins_V1))
				sum_ins_V1 = ''.join(re.findall(r'\d+',sum_ins_V1[5].text))
				print(sum_ins_V1)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit
				elem = driver.find_element(By.XPATH, '//input[@name="givenNamePolicyholder"]')
				elem.clear()
				elem.send_keys(cm_name)
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="mainContactPolicyholder"]')
				elem.clear()
				elem.send_keys(cm_phone)
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="emailPolicyholder"]')
				elem.clear()
				elem.send_keys(cm_email)
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 950);") # scroll down a bit
				elem = driver.find_element(By.XPATH, '//a[@data-ng-click="onBtnNextClicked()"]')
				elem.click()
				time.sleep(sleep_time)
# ===============================================================================================================================================================================
# 
# 				////////////// page: disable deductable ////////////
# 
# ===============================================================================================================================================================================
				deduc_button = ''
				while len(deduc_button) == 0:
					deduc_button = driver.find_elements(By.XPATH, '//button[@data-ng-click="selectedCoverage.ExcessLevelId = i.key;dLCE(12,(selectedCoverage.excess|filter:{key:selectedCoverage.ExcessLevelId})[0].value);"]')
					time.sleep(find_elem_time)
					print('finding deduc buttton')
				deduc_button[0].click()
				time.sleep(sleep_time)


				nc_dis = ''
				while len(nc_dis) == 0:
					nc_dis = driver.find_elements(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]')
					time.sleep(find_elem_time)
					print('finding no claim discount dropdown')
				nc_dis_option = ''
				while len(nc_dis_option) == 0:
					nc_dis_option = driver.find_elements(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]/option[@value="1"]')
					time.sleep(find_elem_time)
					print('finding 20 percent discount')
				select = Select(driver.find_element(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				drv_exp = ''
				while len(drv_exp) == 0:
					drv_exp = driver.find_elements(By.XPATH, '//select[@id="mainDriverDrivingExp"]')
					time.sleep(find_elem_time)
					print('finding drv exp')
				drv_exp_option = ''
				while len(drv_exp_option) == 0:
					drv_exp_option = driver.find_elements(By.XPATH, '//select[@id="mainDriverDrivingExp"]/option[@value="6"]')
					time.sleep(find_elem_time)
					print('finding more 5 years drv exp')
				select = Select(driver.find_element(By.XPATH, '//select[@id="mainDriverDrivingExp"]'))
				select.select_by_value("6")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit		
				time.sleep(sleep_time)


				num_acci = ''
				while len(num_acci) == 0:
					num_acci = driver.find_elements(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]')
					time.sleep(find_elem_time)
					print('finding num accident')
				num_acci_option = ''
				while len(num_acci_option) == 0:
					num_acci_option = driver.find_elements(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]/option[@value="1000003"]')
					time.sleep(find_elem_time)
					print('finding zore accident')
				select = Select(driver.find_element(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]'))
				select.select_by_value("1000003")
				time.sleep(sleep_time)


				recommend_button = ''
				while len(recommend_button) == 0:
					recommend_button = driver.find_elements(By.XPATH, '''//button[@data-ng-class="{'active': (asset.UseMyWorkshop==false ||asset.UseMyWorkshop==0), 'da-override-font-size1': HKLocale.getLocale() === 'th-th'}"]''')
					time.sleep(find_elem_time)
					print('finding recommend button')
				recommend_button[0].click()
				time.sleep(sleep_time)


				ok_to_dismiss_recommend = ''
				while len(ok_to_dismiss_recommend) == 0:
					ok_to_dismiss_recommend = driver.find_elements(By.XPATH, '//a[@class="btn btn-block da-override-btn-green da-override-btn-big"]')
					time.sleep(find_elem_time)
					print('finding ok button')
					print(len(ok_to_dismiss_recommend))
				ok_to_dismiss_recommend[0].click()
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 800);") # scroll down a bit		
				time.sleep(sleep_time)


				select = Select(driver.find_element(By.XPATH, '//select[@id="prevInsurerPolicyholder"]'))
				select.select_by_value("134351")
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="currentPolicyNumber"]')
				elem.clear()
				elem.send_keys(currentPolicyNumber)
				time.sleep(sleep_time)
				

				select = Select(driver.find_element(By.XPATH, '//select[@id="PrevNcdLevelId"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 1200);") # scroll down a bit		
				time.sleep(sleep_time)
				

				elem = driver.find_element(By.XPATH, '//button[@data-ng-click="onBtnNextClicked()"]')
				elem.click()
				time.sleep(sleep_time)
				
# ===============================================================================================================================================================================
# 
# 				////////////// page: input address //////////////
# 
# ===============================================================================================================================================================================
				
				wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
				while len(wait_modal) > 0:
					wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
					time.sleep(find_elem_time)
					print('waiting for waiting modal')

				
				plateNo = ''
				while len(plateNo) == 0:
					plateNo = driver.find_elements(By.XPATH, '//input[@name="vehicleRegNo"]')
					time.sleep(find_elem_time)
					print('finding input num plate')
				plateNo[0].clear()
				plateNo[0].send_keys('Bangkok')
				time.sleep(sleep_time)


				provinceId = ''
				while len(provinceId) == 0:
					provinceId = driver.find_elements(By.XPATH, '//select[@name="LicenseProvinceId"]')
					time.sleep(find_elem_time)
					print('finding province id')
				provinceId_option = ''
				while len(provinceId_option) == 0:
					provinceId_option = driver.find_elements(By.XPATH, '//select[@name="LicenseProvinceId"]/option[@value="0"]')
					time.sleep(find_elem_time)
					print('finding province option')
				select = Select(driver.find_element(By.XPATH, '//select[@name="LicenseProvinceId"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit		
				time.sleep(sleep_time)


				
				body_serial_no = ''
				while len(body_serial_no) == 0:
					body_serial_no = driver.find_elements(By.XPATH, '//input[@name="vehicleChassisNo"]')
					time.sleep(find_elem_time)
					print('finding body serial no')
				body_serial_no[0].clear()
				body_serial_no[0].send_keys('abcde12345')
				time.sleep(sleep_time)



				
				eng_serial_no = ''
				while len(eng_serial_no) == 0:
					eng_serial_no = driver.find_elements(By.XPATH, '//input[@name="vehicleEngineNo"]')
					time.sleep(find_elem_time)
					print('finding eng no')
				eng_serial_no[0].clear()
				eng_serial_no[0].send_keys('abcde12345')
				time.sleep(sleep_time)
				


				premiumV1 = driver.find_elements(By.XPATH, '//span[@class="ng-binding da-override-premium-font-size"]')
				while len(premiumV1) == 0 or len(premiumV1[0].text) <= 5:
					premiumV1 = driver.find_elements(By.XPATH, '//span[@class="ng-binding da-override-premium-font-size"]')
					time.sleep(find_elem_time)
					print('finding premiumV1')
				premiumV1 = float(''.join(re.findall(r'\d+',premiumV1[0].text)))/100
				print(premiumV1)


				time.sleep(sleep_time)


				# ========= backward for doing V52 =========

				driver.back()
				time.sleep(sleep_time)


				wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
				while len(wait_modal) > 0:
					wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
					time.sleep(find_elem_time)
					print('waiting for waiting modal')

				driver.back()
				time.sleep(sleep_time)

				# ========================================================
				# 
				# 		///////////  ins type V52 ///////////
				# 
				# ========================================================

				ins_type = ''
				while len(ins_type) == 0:
					ins_type = driver.find_elements(By.XPATH, '''//button[@ng-click="selectCoverage(c); dLCE(10,c.Name);"]''')
					time.sleep(find_elem_time)
					print('finding V2+')
				ins_type[1].click()
				time.sleep(sleep_time)
				time.sleep(sleep_time)

# ========================= sum ins V2+ ================================
				sum_ins_V52 = driver.find_elements(By.XPATH, '''//span[@data-ng-if="sumInsured.visible"]/span[@data-ng-class="{'da-override-font-size1': HKLocale.getLocale() === 'th-th'}"]''')
				print(len(sum_ins_V52))
				sum_ins_V52 = ''.join(re.findall(r'\d+',sum_ins_V52[6].text))
				print(sum_ins_V52)
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit
				elem = driver.find_element(By.XPATH, '//input[@name="givenNamePolicyholder"]')
				elem.clear()
				elem.send_keys(cm_name)
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="mainContactPolicyholder"]')
				elem.clear()
				elem.send_keys(cm_phone)
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="emailPolicyholder"]')
				elem.clear()
				elem.send_keys(cm_email)
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 950);") # scroll down a bit
				elem = driver.find_element(By.XPATH, '//a[@data-ng-click="onBtnNextClicked()"]')
				elem.click()
				time.sleep(sleep_time)

# ===============================================================================================================================================================================
# 				///////////////////// second time //////////////////
# 				////////////// page: disable deductable ////////////
# 
# ===============================================================================================================================================================================


				nc_dis = ''
				while len(nc_dis) == 0:
					nc_dis = driver.find_elements(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]')
					time.sleep(find_elem_time)
					print('finding no claim discount dropdown')
				nc_dis_option = ''
				while len(nc_dis_option) == 0:
					nc_dis_option = driver.find_elements(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]/option[@value="1"]')
					time.sleep(find_elem_time)
					print('finding 20 percent discount')
				select = Select(driver.find_element(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				drv_exp = ''
				while len(drv_exp) == 0:
					drv_exp = driver.find_elements(By.XPATH, '//select[@id="mainDriverDrivingExp"]')
					time.sleep(find_elem_time)
					print('finding drv exp')
				drv_exp_option = ''
				while len(drv_exp_option) == 0:
					drv_exp_option = driver.find_elements(By.XPATH, '//select[@id="mainDriverDrivingExp"]/option[@value="6"]')
					time.sleep(find_elem_time)
					print('finding more 5 years drv exp')
				select = Select(driver.find_element(By.XPATH, '//select[@id="mainDriverDrivingExp"]'))
				select.select_by_value("6")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit		
				time.sleep(sleep_time)


				num_acci = ''
				while len(num_acci) == 0:
					num_acci = driver.find_elements(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]')
					time.sleep(find_elem_time)
					print('finding num accident')
				num_acci_option = ''
				while len(num_acci_option) == 0:
					num_acci_option = driver.find_elements(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]/option[@value="1000003"]')
					time.sleep(find_elem_time)
					print('finding num accident option')
				select = Select(driver.find_element(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]'))
				select.select_by_value("1000003")
				time.sleep(sleep_time)
				

				recommend_button = ''
				while len(recommend_button) == 0:
					recommend_button = driver.find_elements(By.XPATH, '''//button[@data-ng-class="{'active': (asset.UseMyWorkshop==false ||asset.UseMyWorkshop==0), 'da-override-font-size1': HKLocale.getLocale() === 'th-th'}"]''')
					time.sleep(find_elem_time)
					print('finding recommend button')
				recommend_button[0].click()
				time.sleep(sleep_time)


				ok_to_dismiss_recommend = ''
				while len(ok_to_dismiss_recommend) == 0:
					ok_to_dismiss_recommend = driver.find_elements(By.XPATH, '//a[@class="btn btn-block da-override-btn-green da-override-btn-big"]')
					time.sleep(find_elem_time)
					print('finding ok button')
					print(len(ok_to_dismiss_recommend))
				ok_to_dismiss_recommend[0].click()
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 800);") # scroll down a bit		
				time.sleep(sleep_time)


				select = Select(driver.find_element(By.XPATH, '//select[@id="prevInsurerPolicyholder"]'))
				select.select_by_value("134351")
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="currentPolicyNumber"]')
				elem.clear()
				elem.send_keys(currentPolicyNumber)
				time.sleep(sleep_time)
				

				select = Select(driver.find_element(By.XPATH, '//select[@id="PrevNcdLevelId"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 1200);") # scroll down a bit		
				time.sleep(sleep_time)
				

				elem = driver.find_element(By.XPATH, '//button[@data-ng-click="onBtnNextClicked()"]')
				elem.click()
				time.sleep(sleep_time)

# ===============================================================================================================================================================================
# 				///////////////////// second time ///////////////
# 				////////////// page: input address //////////////
# 
# ===============================================================================================================================================================================
				
				wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
				while len(wait_modal) > 0:
					wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
					time.sleep(find_elem_time)
					print('waiting for waiting modal')


				plateNo = ''
				while len(plateNo) == 0:
					plateNo = driver.find_elements(By.XPATH, '//input[@name="vehicleRegNo"]')
					time.sleep(find_elem_time)
					print('finding input plate no')
				plateNo[0].clear()
				plateNo[0].send_keys('Bangkok')
				time.sleep(sleep_time)


				provinceId = ''
				while len(provinceId) == 0:
					provinceId = driver.find_elements(By.XPATH, '//select[@name="LicenseProvinceId"]')
					print('finding province id')
					time.sleep(find_elem_time)
				provinceId_option = ''
				while len(provinceId_option) == 0:
					provinceId_option = driver.find_elements(By.XPATH, '//select[@name="LicenseProvinceId"]/option[@value="0"]')
					print('finding province option')
					time.sleep(find_elem_time)
				select = Select(driver.find_element(By.XPATH, '//select[@name="LicenseProvinceId"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit		
				time.sleep(sleep_time)


				
				body_serial_no = ''
				while len(body_serial_no) == 0:
					body_serial_no = driver.find_elements(By.XPATH, '//input[@name="vehicleChassisNo"]')
					time.sleep(find_elem_time)
					print('finding body no')
				body_serial_no[0].clear()
				body_serial_no[0].send_keys('abcde12345')
				time.sleep(sleep_time)



				
				eng_serial_no = ''
				while len(eng_serial_no) == 0:
					eng_serial_no = driver.find_elements(By.XPATH, '//input[@name="vehicleEngineNo"]')
					time.sleep(find_elem_time)
					print('finding eng no')
				eng_serial_no[0].clear()
				eng_serial_no[0].send_keys('abcde12345')
				time.sleep(sleep_time)


				

				premiumV52 = driver.find_elements(By.XPATH, '//span[@class="ng-binding da-override-premium-font-size"]')
				while len(premiumV52) == 0 or len(premiumV52[0].text) <= 5:
					premiumV52 = driver.find_elements(By.XPATH, '//span[@class="ng-binding da-override-premium-font-size"]')
					time.sleep(find_elem_time)
					print('finding premium V2+')
				premiumV52 = float(''.join(re.findall(r'\d+',premiumV52[0].text)))/100
				print(premiumV52)


				time.sleep(sleep_time)


				# ========= backward for doing V53 =========


				driver.back()
				time.sleep(sleep_time)


				wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
				while len(wait_modal) > 0:
					wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
					time.sleep(find_elem_time)
					print('waiting for waiting modal')


				driver.back()
				time.sleep(sleep_time)

				# ========================================================
				# 
				# 		///////////  ins type V53 ///////////
				# 
				# ========================================================

				ins_type = ''
				while len(ins_type) == 0:
					ins_type = driver.find_elements(By.XPATH, '''//button[@ng-click="selectCoverage(c); dLCE(10,c.Name);"]''')
					time.sleep(find_elem_time)
					print('finding V3+')
				ins_type[2].click()
				time.sleep(sleep_time)
				time.sleep(sleep_time)

# ========================= sum ins V3+ ================================

				sum_ins_V53 = driver.find_elements(By.XPATH, '''//span[@data-ng-if="sumInsured.visible"]/span[@data-ng-class="{'da-override-font-size1': HKLocale.getLocale() === 'th-th'}"]''')
				print(len(sum_ins_V53))
				sum_ins_V53 = ''.join(re.findall(r'\d+',sum_ins_V53[7].text))
				print(sum_ins_V53)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit
				elem = driver.find_element(By.XPATH, '//input[@name="givenNamePolicyholder"]')
				elem.clear()
				elem.send_keys(cm_name)
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="mainContactPolicyholder"]')
				elem.clear()
				elem.send_keys(cm_phone)
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="emailPolicyholder"]')
				elem.clear()
				elem.send_keys(cm_email)
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 950);") # scroll down a bit
				elem = driver.find_element(By.XPATH, '//a[@data-ng-click="onBtnNextClicked()"]')
				elem.click()
				time.sleep(sleep_time)

# ===============================================================================================================================================================================
# 				///////////////////// third time ///////////////////
# 				////////////// page: disable deductable ////////////
# 
# ===============================================================================================================================================================================


				nc_dis = ''
				while len(nc_dis) == 0:
					nc_dis = driver.find_elements(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]')
					time.sleep(find_elem_time)
					print('finding no claim discount')
				nc_dis_option = ''
				while len(nc_dis_option) == 0:
					nc_dis_option = driver.find_elements(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]/option[@value="1"]')
					time.sleep(find_elem_time)
					print('finding no claim discount option')
				select = Select(driver.find_element(By.XPATH, '//select[@id="noClaimDiscountAtRenewal"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				drv_exp = ''
				while len(drv_exp) == 0:
					drv_exp = driver.find_elements(By.XPATH, '//select[@id="mainDriverDrivingExp"]')
					time.sleep(find_elem_time)
					print('finding drv exp')
				drv_exp_option = ''
				while len(drv_exp_option) == 0:
					drv_exp_option = driver.find_elements(By.XPATH, '//select[@id="mainDriverDrivingExp"]/option[@value="6"]')
					time.sleep(sleep_time)
					print('finding more 5 years drv exp')
				select = Select(driver.find_element(By.XPATH, '//select[@id="mainDriverDrivingExp"]'))
				select.select_by_value("6")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit		
				time.sleep(sleep_time)


				num_acci = ''
				while len(num_acci) == 0:
					num_acci = driver.find_elements(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]')
					time.sleep(find_elem_time)
					print('finding num accident')
				num_acci_option = ''
				while len(num_acci_option) == 0:
					num_acci_option = driver.find_elements(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]/option[@value="1000003"]')
					time.sleep(find_elem_time)
					print('finding num accident option')
				select = Select(driver.find_element(By.XPATH, '//select[@id="accidentsInThreeYearsMD"]'))
				select.select_by_value("1000003")
				time.sleep(sleep_time)
				

				recommend_button = ''
				while len(recommend_button) == 0:
					recommend_button = driver.find_elements(By.XPATH, '''//button[@data-ng-class="{'active': (asset.UseMyWorkshop==false ||asset.UseMyWorkshop==0), 'da-override-font-size1': HKLocale.getLocale() === 'th-th'}"]''')
					time.sleep(find_elem_time)
					print('finding recommend button')
				recommend_button[0].click()
				time.sleep(sleep_time)


				ok_to_dismiss_recommend = ''
				while len(ok_to_dismiss_recommend) == 0:
					ok_to_dismiss_recommend = driver.find_elements(By.XPATH, '//a[@class="btn btn-block da-override-btn-green da-override-btn-big"]')
					time.sleep(find_elem_time)
					print('finding ok button')
					print(len(ok_to_dismiss_recommend))
				ok_to_dismiss_recommend[0].click()
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 800);") # scroll down a bit		
				time.sleep(sleep_time)


				select = Select(driver.find_element(By.XPATH, '//select[@id="prevInsurerPolicyholder"]'))
				select.select_by_value("134351")
				time.sleep(sleep_time)


				elem = driver.find_element(By.XPATH, '//input[@name="currentPolicyNumber"]')
				elem.clear()
				elem.send_keys(currentPolicyNumber)
				time.sleep(sleep_time)
				

				select = Select(driver.find_element(By.XPATH, '//select[@id="PrevNcdLevelId"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 1200);") # scroll down a bit		
				time.sleep(sleep_time)
				

				elem = driver.find_element(By.XPATH, '//button[@data-ng-click="onBtnNextClicked()"]')
				elem.click()
				time.sleep(sleep_time)

# ===============================================================================================================================================================================
# 				///////////////////// third time ////////////////
# 				////////////// page: input address //////////////
# 
# ===============================================================================================================================================================================
				
				wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
				while len(wait_modal) > 0:
					wait_modal = driver.find_elements(By.XPATH, '//div[@id="daLoadingMask"][@aria-hidden="false"]')
					time.sleep(find_elem_time)
					print('waiting for waiting modal')



				plateNo = ''
				while len(plateNo) == 0:
					plateNo = driver.find_elements(By.XPATH, '//input[@name="vehicleRegNo"]')
					time.sleep(find_elem_time)
					print('finding input plate no')
				plateNo[0].clear()
				plateNo[0].send_keys('Bangkok')
				time.sleep(sleep_time)


				provinceId = ''
				while len(provinceId) == 0:
					provinceId = driver.find_elements(By.XPATH, '//select[@name="LicenseProvinceId"]')
					time.sleep(find_elem_time)
					print('finding province id')
				provinceId_option = ''
				while len(provinceId_option) == 0:
					provinceId_option = driver.find_elements(By.XPATH, '//select[@name="LicenseProvinceId"]/option[@value="0"]')
					time.sleep(find_elem_time)
					print('finding province option')
				select = Select(driver.find_element(By.XPATH, '//select[@name="LicenseProvinceId"]'))
				select.select_by_value("1")
				time.sleep(sleep_time)


				driver.execute_script("window.scrollTo(0, 500);") # scroll down a bit		
				time.sleep(sleep_time)


				
				body_serial_no = ''
				while len(body_serial_no) == 0:
					body_serial_no = driver.find_elements(By.XPATH, '//input[@name="vehicleChassisNo"]')
					time.sleep(find_elem_time)
					print('finding body no')
				body_serial_no[0].clear()
				body_serial_no[0].send_keys('abcde12345')
				time.sleep(sleep_time)



				
				eng_serial_no = ''
				while len(eng_serial_no) == 0:
					eng_serial_no = driver.find_elements(By.XPATH, '//input[@name="vehicleEngineNo"]')
					time.sleep(find_elem_time)
					print('finding eng no')
				eng_serial_no[0].clear()
				eng_serial_no[0].send_keys('abcde12345')
				time.sleep(sleep_time)



				premiumV53 = driver.find_elements(By.XPATH, '//span[@class="ng-binding da-override-premium-font-size"]')
				while len(premiumV53) == 0 or len(premiumV53[0].text) <= 5:
					premiumV53 = driver.find_elements(By.XPATH, '//span[@class="ng-binding da-override-premium-font-size"]')
					time.sleep(find_elem_time)
					print('finding premium V3+')
				premiumV53 = float(''.join(re.findall(r'\d+',premiumV53[0].text)))/100
				print(premiumV53)


				time.sleep(sleep_time)


				garage_str = list_red_key[i][j] + ',' + list_car_brand[i] + ',' + list_car_model[i] + ',' + list_car_make_year[i][j] + ',' + 'GARAGE' + ',' + list_cm_age[x] + ',' + list_cm_sex[k] + ',' + 'DirectAsia' + ',' + str(sum_ins_V1) + ',' + str(premiumV1) + ',' + str(sum_ins_V52) + ',' + str(premiumV52) + ',' + str(sum_ins_V53) + ',' + str(premiumV53) + ',' + 'V52 and V53 including deductable(2000)\n'
				# dealer_str = list_red_key[i][j] + ',' + list_car_brand[i] + ',' + list_car_model[i] + ',' + list_car_make_year[i][j] + ',' + 'DEALER' + ',' + list_cm_age[x] + ',' + list_cm_sex[k] + ',' + 'DirectAsia' + ',' + str(sum_ins_V1) + ',' + str(premiumV1) + ',' + str(sum_ins_V52) + ',' + str(premiumV52) + ',' + str(sum_ins_V53) + ',' + str(premiumV53) + ',' + 'V52 and V53 including deductable(2000)\n'
				f = open('directAsia_version2_data.csv','a')
				f.write(garage_str)
				# f.write(dealer_str)
				f.close()
				print(garage_str)
				# print(dealer_str)

				driver.close()
print("complete")


