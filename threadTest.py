from PyQt5.QtCore import *
from selenium import webdriver
from time import sleep
import csv
class Threadd(QThread):
    salary = pyqtSignal(str)
    name = pyqtSignal(str)

    def __init__(self):
        super(Threadd,self).__init__()
        self.isRunning = True
    def run(self):
        try:
            while True:
                self.driver = webdriver.Firefox()
                with open('data.csv', newline='') as f:
                    EAN =csv.DictReader(f)
                    for ean in EAN:
                        self.driver.get(f"https://egypt.souq.com/eg-ar/{ean['ean']}/s/?as=1") 
                        self.elms = self.driver.find_elements_by_xpath("/html/body/div[2]/div/main/div[2]/div/header/div[2]/div[2]/div[2]/div[1]/div/h1")
                        self.els = self.driver.find_elements_by_xpath("/html/body/div[2]/div/main/div[2]/div/header/div[2]/div[2]/div[3]/div/section/div/div/div[1]/h3")
                        for self.i in self.els:
                            sleep(0.02)
                            self.salary.emit(f'=> {self.i.text}\n')
                        for self.e in self.elms:
                            sleep(0.02)
                            self.name.emit(f'=> {self.e.text}\n')
                        with open('demo.txt','a') as f:
                            f.write(f"{self.i.text} == {self.e.text}\n")
                            f.close()
        except:
            pass
        self.wait()
        self.quit()
