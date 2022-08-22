import gradio as gr
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

url = 'https://raw.githubusercontent.com/ArushiS12/gradio-heroku/main/Zomato-Chennai.csv'
data = pd.read_csv(url)

def cuisine(Cuisine,Area):
    l = [Cuisine]
    x=data['Cuisine'].str.contains('|'.join(l))
    data['Flag'] = np.where(x, 'Yes', 'No')
    df = data.loc[data['Flag'] == 'Yes']
    if Area:
        df1 = df[df['Area'] == Area]
        final1 = df1.drop('Flag', axis=1)
        return final1
    else:
        final = df.drop('Flag', axis=1)
        return final
        
cuisine_options = ['American','Andhra','Arabian','Asian','Bakery','Bar Food','BBQ','Beverages','Biryani','Bubble Tea','Burger','Burmese','Cafe','Charcoal Chicken','Chettinad','Chinese','Coffee','Continental','Desserts','Drinks Only','European','Fast Food','Finger Food','French','Gujarati','Healthy Food','Hyderabadi','Ice Cream','Irish','Italian','Japanese','Juices','Kebab','Kerala','Konkan','Korean','Lebanese','Malaysian','Mangalorean','Mediterranean','Mexican','Middle Eastern','Mithai','Modern Indian','Momos','Mughlai','North Indian','Oriental','Pancake','Pasta','Pizza','Rajasthani','Rolls','Salad','Sandwich','Seafood','Shake','Sichuan','Singaporean','South Indian','Spanish','Steak','Street Food','Sushi','Tamil','Tea','Tex-Mex','Thai','Tibetan','Turkish','Vietnamese','Waffle','Wraps']
area_options = ['Abhiramapuram','Adyar','Akkarai','Alandur','Alwarpet','Ambattur','Ampa Skywalk Mall Aminijikarai','Anna Nagar East','Anna Nagar West','Anna Salai','Arumbakkam','Ashok Nagar','Avadi','Besant Nagar','Chetpet','Choolaimed','Chromepet','Citadines','Courtyard by Marriott Teynampet','Crowne Plaza Adyar Park Alwarpet','E Hotel Royapettah','Egatoor','Egmore','Ekkaduthangal','Feathers A Radha Hotel','Foodies Kitchen','Forum Vijaya Mall Vadapalani','George Town','Gopalapuram','Grand by GRT Hotels','Green Park Hotel Vadapalani','GST Road','Guindy','Hablis Hotel Guindy','Hilton Guindy','Holiday Inn OMR IT Expressway','Hotel Abu Palace Egmore','Hotel Maris Gopalapuram','Hotel Palmgrove Nungambakkam','Hotel Park Elanza Nungambakkam','Hotel Rajpark Alwarpet','Hyatt Regency Teynampet','IBIS OMR','Injambakkam','Ispahani Centre Nungambakkam','InterContinental  Mahabalipuram Resort East Coast Road (ECR)','ITC Grand Chola Guindy','Jaag Hotels T.Nagar','K.K. Nagar','Kanathur','Karapakkam','Kilpauk','Kipling East Coast Road (ECR)','Kodambakkam','Kolathur','Kotturpuram','Kovalam','Lemon Tree Hotel Guindy','Madipakkam','Maduravoyal','Mahabalipuram','Mandaveli','Medavakkam','Meenambakkam','Mogappair','MRC Nagar','Muttukadu','Mylapore','Nandanam','Navallur','Neelangarai','New Woodlands Hotel Mylapore','Novotel  Nandanam','Novotel  OMR','Nungambakkam','Okkiyampet','Old Mahabalipuram Road (OMR)','OMR Food Street Kandanchavadi','Paati Veedu T.Nagar','Palavakkam','Pallikaranai','Perambur','Perungudi','Phoenix Market City Velachery','Poonamalle','Porur','Potheri','Purasavakkam','RA Puram','Radisson Blu Egmore','Radisson Blu Temple Bay Mamallapuram','Ramada Plaza Guindy','Ramapuram','Royapettah','Saidapet','Saligramam','Selaiyur','Semmancheri','Sheraton Grand Neelangarai','Sholinganallur','Somerset Greenways','St. Thomas Mount','T. Nagar','Taj Club House Thousand Lights','Taj Coromandel Nungambakkam',"Taj Fisherman's Cove Resort & Spa Kanchipuram District",'Tambaram','Taramani','Teynampet','The Accord Metropolitan T. Nagar',"The King's Hotel Egmore",'The Leela Palace MRC Nagar','The Park Nungambakkam','The Raintree Alwarpet','The Residency T. Nagar','The Residency Towers T. Nagar','The Savara Hotel RK Salai (Cathedral Road)','The Westin Velachery','Thiruvanmiyur','Thousand Lights','Thuraipakkam','Tiruvottiyur','Triplicane','Turyaa','Vadapalani','Valasaravakkam','Velachery','Vepery','Virugambakkam','VR Mall Anna Nagar','Washermenpet','West Mambalam','Zone by The Park Pallikaranai']

with gr.Blocks() as demo:
    gr.Markdown("<h1><center>Dine-out Restaurants in Chennai</center></h1>")
    gr.Markdown('<h3><span style="font-weight:normal">Search for your nearby restaurants.</span></h3>')

    with gr.Row():
        name = gr.Dropdown(cuisine_options,label="Cuisine")
        name1 = gr.Dropdown(area_options,label="Location")
        
    with gr.Row():
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")
        
    output = gr.DataFrame(label="Restaurants",wrap=True)
    
    submit_btn.click(fn=cuisine, inputs=[name,name1], outputs=output)
    clear_btn.click(None,inputs=[],outputs=output, _js="() => (null)\n")
    
demo.launch()
