# This script focuses on building dash app.

from dash import Input, Output, State, dcc, html, Dash  # componenets used to create the dash-app 
import dash_bootstrap_components as dbc  # to get theme for the app
from plot_data import Plot  # for plotting graphs
from model import Model  # for making predictions

# initialize the Plot
plot = Plot()

# initialize the Model
model = Model()

# load the saved model
model.load()

# get the graph for feature importances
fig = plot.feats_imp(model=model)

# Initiallze the Dash with theme
app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# get the body of dash-app
body = dbc.Container([ 
                dbc.Row([
                        # Header
                        html.H1("Used Auction Cars Data", style={"padding-left": "350px", "padding-top": "50px"}),
                        
                        # Exploratory Data Analysis 
                        html.Div([

                        html.H4("Please Select a feature to compare to Selling Price:", style={"margin-top": "50px"}),
                        # Drop-down menu for selecting the graphs
                        dcc.Dropdown(
                            options=["Manufacturer", "Body Type", "Condition", "Odometer", "Car Age", "Buying Year", "MMR"],
                            value="MMR",
                            searchable=False,
                            placeholder="Select a Feature to compare with Selling Price.",
                            id="plots-dropdown",
                            style={"color": "Black"}
                        )
                        ]),
                        # Plot the figure
                        html.Div(id="plot-display", style={"padding-left":"200px"}),
                        # Header
                        html.H1("Auction Cars Price Predictor", style={"padding-left": "330px", "padding-top": "50px", "padding-bottom": "50px"}),
                        # Warning for using the trained model
                        html.H5("Warning: It is a Tree Model, so some inconsistencies are expected.", style={"padding-bottom": "50px"}),
                        # Graph for feature importances
                        html.Div(dcc.Graph(figure=fig), style={"padding-bottom": "50px", "padding-left": "200px"}),
                        
                        # Getting the predictor variables
                        html.Div([
                            
                            html.H5("Buying Year:"),
                            # Slider for getting the buying-year
                            dcc.Slider(1990, 2015, 1, value=2015, marks=None,
                                       tooltip={"placement": "bottom", "always_visible": True}, id="buy-slide"),
                            
                            html.H5("Age of the Car:", style={"margin-top": "10px"}),
                            # Slider for getting the age of the car
                            dcc.Slider(0, 25, 1, value=25, marks=None,
                                       tooltip={"placement": "bottom", "always_visible": True}, id="age-slide"),
                            
                            html.H5("Manheim Market Report [MMR]:", style={"margin-top": "10px"}),
                            # Slider for getting the MMR
                            dcc.Slider(25, 200000, 25, value=10000, marks=None,
                                       tooltip={"placement": "bottom", "always_visible": True}, id="mmr-slide"),
                            
                            html.H5("Odometer [miles]:", style={"margin-top": "10px"}),
                            # Slider for getting the odometer
                            dcc.Slider(0, 250000, 50, value=10000, marks=None,
                                       tooltip={"placement": "bottom", "always_visible": True}, id="odometer-slide"),
                            
                            html.H5("Condition of the Car:", style={"margin-top": "10px"}),
                            # Slider for getting the condition of the car
                            dcc.Slider(0, 7, 0.2, value=7, marks=None,
                                       tooltip={"placement": "bottom", "always_visible": True}, id="condition-slide"),
                            
                            html.H5("Body Type:", style={"margin-top": "10px"}),
                            # Drop-down menu for getting the body-type of the car
                            dcc.Dropdown(
                                options=[
                                    {"label": "SUV", "value": "suv"},
                                    {"label": "Sedan", "value": "sedan"}, 
                                    {"label": "Convertible", "value": "convertible"}, 
                                    {"label": "Coupe", "value": "coupe"},
                                    {"label": "Koup", "value": "Koup"}, 
                                    {"label": "Wagon", "value": "Wagon"},
                                    {"label": "Hatchback", "value": "hatchback"},
                                    {"label": "Cab", "value": "cab"},
                                    {"label": "Van", "value": "van"},
                                    {"label": "SuperCrew", "value": "supercrew"},
                                ],
                                value="suv",
                                searchable=False,
                                placeholder="Select Body Type!",
                                id="body-dropdown",
                                style={"color": "Black"}
                            ),
                            
                            html.H5("Car's Manufacturer:", style={"margin-top": "10px"}),
                            # Drop-down menu for getting the car's manufacturer
                            dcc.Dropdown(
                                options=[
                                    'acura', 'aston martin', 'audi', 'bentley', 'bmw', 'buick', 'cadillac', 'chevrolet',
                                    'chrysler', 'daewoo', 'dodge', 'ferrari', 'fiat', 'fisker', 'ford', 'geo', 'gmc', 'honda',
                                    'hummer', 'hyundai', 'infiniti', 'isuzu', 'jaguar', 'jeep','kia', 'lamborghini',
                                    'land rover', 'lexus', 'lincoln', 'lotus', 'maserati', 'mazda', 'mercedes', 'mercury',
                                    'mini', 'mitsubishi', 'nissan', 'oldsmobile', 'plymouth', 'pontiac', 'porsche', 'ram',
                                    'rolls-royce', 'saab', 'saturn', 'scion', 'smart', 'subaru', 'suzuki', 'tesla',
                                    'toyota', 'volkswagen', 'volvo'
                                ],
                                value="acura",
                                searchable=False,
                                placeholder="Select a Manufacturer!",
                                id="make-dropdown",
                                style={"color": "Black"}
                            ),
                            
                            html.H5("State of the Car:", style={"margin-top": "10px"}),
                            # Drop-down menu for getting the state of the car
                            dcc.Dropdown(
                                options=[
                                    'ab', 'al', 'az', 'ca', 'co', 'fl', 'ga', 'hi', 'il', 'in', 'la',
                                    'ma', 'md', 'mi', 'mn', 'mo', 'ms', 'nc', 'ne', 'nj', 'nm', 'ns',
                                    'nv', 'ny', 'oh', 'ok', 'on', 'or', 'pa', 'pr', 'qc', 'sc', 'tn',
                                    'tx', 'ut', 'va', 'wa', 'wi'
                                ],
                                value="ab",
                                searchable=False,
                                placeholder="Select State of the Car!",
                                id="state-dropdown",
                                style={"color": "Black"}
                            ),
                            
                            html.H5("Color of the Car:", style={"margin-top": "10px"}),
                            # Drop-down menu for getting the color of the car
                            dcc.Dropdown(
                            options=[
                                    'beige', 'black', 'blue', 'brown', 'burgundy', 'charcoal', 'gold',
                                    'gray', 'green', 'lime', 'off-white', 'orange', 'other', 'pink',
                                    'purple', 'red', 'silver', 'turquoise', 'white', 'yellow'
                                ],
                                value="black",
                                searchable=False,
                                placeholder="Select Color of the Car!",
                                id="color-dropdown",
                                style={"color": "Black"}
                            ),
                            
                            html.Div(id="pred-text", style={"margin-top": "20px", "margin-bottom": "40px"})
                            
                        ])
 
                ])], style={"height": "100vh"}
)

# apply the body to the dash-app's layout
app.layout = html.Div([body])

# create a callback for getting the graphs
@app.callback(
Output("plot-display", "children"),
Input("plots-dropdown", "value")
)
def display(graph_name):
    """This function take the name of the graph and then returns the plotly.px `fig`."""
    
    if graph_name == "Manufacturer":
        fig = plot.sell_make()
        return dcc.Graph(figure=fig)
    
    if graph_name == "Body Type":
        fig = plot.sell_body()
        return dcc.Graph(figure=fig)
    
    if graph_name == "Condition":
        fig = plot.sell_condition()
        return dcc.Graph(figure=fig)
    
    if graph_name == "Odometer":
        fig = plot.sell_odometer()
        return dcc.Graph(figure=fig)
    
    if graph_name == "Car Age":
        fig = plot.sell_age()
        return dcc.Graph(figure=fig)
    
    if graph_name == "Buying Year":
        fig = plot.sell_bought()
        return dcc.Graph(figure=fig)
    
    if graph_name == "MMR":
        fig = plot.sell_mmr()
        return dcc.Graph(figure=fig)
    

# create a callback for getting the predictions
@app.callback(
Output("pred-text", "children"),
[Input("buy-slide", "value"),
Input("age-slide", "value"),
Input("mmr-slide", "value"),
Input("odometer-slide", "value"),
Input("condition-slide", "value"),
Input("body-dropdown", "value"),
Input("make-dropdown", "value"),
Input("state-dropdown", "value"),
Input("color-dropdown", "value")]
)
def predictor(year, age, mmr, odometer, condition, body, make, state, color):
    """Takes a single test data at a time and performs prediction for the dash app."""
    
    pred = model.predict([[float(year), str(make), str(body), str(state), float(condition), float(odometer), str(color), float(mmr), float(age)]])
    
    # get the prediction ready for the output
    text = f"The Selling Price of the Car is {pred.tolist()[0]}"
    
    return html.H5(text)

    
# run the dash-app
if __name__ == "__main__":
    app.run_server(debug=False)