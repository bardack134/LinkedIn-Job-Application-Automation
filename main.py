from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import EMAIL, LINKEDIN_URL, PASSWORD
from selenium.webdriver.common.keys import Keys


class LinkedInBot:
    def __init__(self):
        
        # Mantener el navegador abierto después de que el script ha sido ejecutado, y ampliar el navegador
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
        
        # Crear objeto webdriver para Chrome
        self.driver = webdriver.Chrome(options=chrome_options)
        #get the website
        self.driver.get(url=LINKEDIN_URL)
        
    
    def navegation(self):
        """Method that  opens the web page, and presses the button to log in in user account."""

        try:
            sing_in_element=self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
            sing_in_element.click()
            
        except Exception as err:
            
            # Imprimir un mensaje de error si ocurre una excepción
            print(f"Error occurred while finding sign in element: {err}")  

        # 2 segundos a que la pag carge
        sleep(2)


    def user_name(self):
        """Method that enter on LinkedIn the  provided email."""
        
        try:
            sign_in=self.driver.find_element(By.ID, "username")
            sign_in.send_keys(EMAIL)
                
        except Exception as err:
            
            # Imprimir un mensaje de error si ocurre una excepción
            print(f"Error occurred while entering the username: {err}")  


    #iniciando seccion en linkedin
    def password(self):
        """Method that enters the password on LinkedIn."""
        
        try:
            sign_in=self.driver.find_element(By.ID, "password")
            sign_in.send_keys(PASSWORD, Keys.ENTER) 
                
        except Exception as err:
            
            # Imprimir un mensaje de error si ocurre una excepción
            print(f"Error occurred while entering password: {err}")  
  
        sleep(6)#espera 6 segundos despues de iniciar session
        
        
    def login(self):
        """Methods that manages the loging process"""
        self.navegation()
        self.user_name()
        self.password()


    def looking_for_jobs(self):
        """"Methods that get all available jobs"""
        
        try:
            #obtenemos la ventana donde se encuntran todos los trabajos disponibles
            self.jobs_container=self.driver.find_element(By.CSS_SELECTOR, value="ul.scaffold-layout__list-container")
            return self.jobs_container
        
        except Exception as err:
            
            # Imprimir un mensaje de error si ocurre una excepción
            print(f"Error occurred while looking for the available jobs: {err}")
    
    
    def apply_job(self):
        """Method that apply to the available jobs founded"""
        
        jobsContainer=self.looking_for_jobs()
        
        #evaluamos si jobContainer tiene algun valor que se considere verdadero
        if jobsContainer:
            
            #buscando dentro de la ventana de trabajos, cada trabajo que muestra la ventana, generando una lista de trabajos
            jobs_list=self.jobs_container.find_elements(By.CSS_SELECTOR, value="li.ember-view")  
            print(f"{len(jobs_list)} jobs were found available.")
            
            
            #itirenando sobre la lista de trabajos en contrados  
            for job in jobs_list:   
                
                sleep(0.4)
                            
                try:
                    #haciendo click en el trabajo
                    job.click() 
                    
                    sleep(1)
                    
                    #trtamos de obtener el boton 'save' despues de hacer click en el trabajo mostrado en la lista
                    button_save=self.jobs_container.find_elements(By.CSS_SELECTOR, value="button.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary")
                    
                    button_save.click()  
                    # print('btton here')      
                                                         
                except Exception as err:
                    
                    # Imprimir un mensaje de error si ocurre una excepción
                    print(f"Error occurred while clicking in the job or  trying to find the botton 'save job': {err}")
                          

        else:
            print("No jobs availables")
            
            
    def run_script(self):
        """method tht run the script"""
        self.login()
        self.apply_job()
        
                
linkedInBot=LinkedInBot()
linkedInBot.run_script()
