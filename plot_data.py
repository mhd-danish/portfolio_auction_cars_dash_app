# This script will be used for plotting

import plotly.express as px  # used for plotting data for dash-app
from wrangle_data import Data, pd  #  get the dataset

class Plot:
    """Takes the wrangled data and returns the plots."""
    def __init__(self, dataframe=Data().wrangle()):
        
        self.df = dataframe #  get the data
        
    def sell_make(self):
        """Plot a car's manufacturer vs selling price graph."""
        
        # get the data ready for plotting
        dataframe=self.df
        tmp = dataframe[~dataframe.make.isin(["other"])].groupby("make").sellingprice.mean().sort_values(ascending=True).tail(10).to_frame().reset_index()
        tmp["make"] = tmp.make.str.capitalize() # capitalize the strings
        
        # get the graph as `fig`
        fig = px.bar(
            data_frame=tmp,
            x="sellingprice",
            y="make",
            width=700,
            height=400,
        )
        
        # update the layout
        fig.update_layout(xaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          yaxis_title=dict(text='<b>'"Manufacturer"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Class",
                          title=dict(text="<b>Selling Prices by Top-10 Manufacturers</b>",
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          hovermode="y"
        )

        fig.update_traces(hovertemplate=None)

        return fig
    
    
    def sell_body(self):
        """Plot a car's body type vs selling price graph."""

        # get the data ready for graph
        dataframe=self.df
        tmp = dataframe[~dataframe.body.isin(["other"])].groupby("body").sellingprice.mean().sort_values(ascending=True).tail(10).to_frame().reset_index()
        tmp["model"] = tmp.body.str.capitalize()
        
        # get the graph as `fig`
        fig = px.bar(
            data_frame=tmp,
            x="sellingprice",
            y="model",
            width=700,
            height=400,
        )
        
        # update the layout
        fig.update_layout(xaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          yaxis_title=dict(text='<b>'"Body Type"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Class",
                          title=dict(text='<b>Selling Price by Top-10 Body-Types</b>',
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          hovermode="y"
        )

        fig.update_traces(hovertemplate=None)

        return fig
    
    def sell_condition(self):
        """Plot a car's condition vs selling price graph."""
        
        # get the data ready for plotting
        dataframe=self.df
        fig = px.scatter(
            data_frame=dataframe.sample(10000),
            y="sellingprice",
            x="condition",
            width=700,
            height=400,
            trendline="lowess",
            color="sellingprice",
            # color_continuous_scale='Bluered_r'
        )

        fig.update_layout(xaxis_title=dict(text='<b>'"Car Condition"'</b>',
                                           font=dict(
                                           size=13)),
                          yaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Class",
                          title=dict(text="<b>Selling Price by Cars' Conditions</b>",
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          coloraxis_colorbar_title_text = 'Selling Price',
                          hovermode="x"
        )

        fig.update_traces(hovertemplate=None)

        return fig
    
    def sell_odometer(self):
        """Plot a car's odometer reading vs selling price graph."""
        
        dataframe=self.df
        fig = px.scatter(
            data_frame=dataframe.sample(10000),
            y="sellingprice",
            x="odometer",
            width=700,
            height=400,
            trendline="lowess",
            color="sellingprice",
        )

        fig.update_layout(xaxis_title=dict(text='<b>'"Odometer [mile]"'</b>',
                                           font=dict(
                                           size=13)),
                          yaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Class",
                          title=dict(text="<b>Selling Price by Odometer</b>",
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          coloraxis_colorbar_title_text = 'Selling Price',
                          hovermode="x"
        )

        fig.update_traces(hovertemplate=None)

        return fig
    
    def sell_color(self):
        """Plot a car's paint color vs selling price graph."""
        
        dataframe=self.df
        tmp = dataframe[~dataframe.color.isin(["other"])].groupby("color").sellingprice.mean().sort_values().to_frame().reset_index()
        tmp["color"] = tmp.color.str.capitalize()

        fig = px.bar(
            data_frame=tmp,
            y="sellingprice",
            x="color",
            width=700,
            height=400,
            color="sellingprice",
            # color_continuous_scale='Dark2'
        )

        fig.update_layout(yaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          xaxis_title=dict(text='<b>'"Paint"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Paint",
                          title=dict(text='<b>Selling Price by Car Paint</b>',
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          hovermode="x"
        )

        fig.update_xaxes(tickangle=-50)

        fig.update_traces(hovertemplate=None)

        return fig
    

    def sell_age(self):
        """Plot a car's age vs selling price graph."""
        
        dataframe=self.df
        fig = px.scatter(
            data_frame=dataframe.sample(10000),
            y="sellingprice",
            x="age_when_sold",
            width=700,
            height=400,
            trendline="lowess",
            color="sellingprice",
        )

        fig.update_layout(xaxis_title=dict(text='<b>'"Car's Age [Year]"'</b>',
                                           font=dict(
                                           size=13)),
                          yaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Class",
                          title=dict(text="<b>Selling Price by Car Age</b>",
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          coloraxis_colorbar_title_text = 'Selling Price',
                          hovermode="x"
        )

        fig.update_traces(hovertemplate=None)

        return fig
    

    def sell_mmr(self):
        """Plot a car's MMR vs selling price graph."""
        
        dataframe=self.df
        fig = px.scatter(
            data_frame=dataframe.sample(10000),
            y="sellingprice",
            x="mmr",
            width=700,
            height=400,
            trendline="ols",
            color="sellingprice",
        )

        fig.update_layout(xaxis_title=dict(text='<b>'"MMR Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          yaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Class",
                          title=dict(text="<b>Selling Price by Manheim Market Report Price</b>",
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          coloraxis_colorbar_title_text = 'Selling Price',
                          hovermode="x"
        )

        fig.update_traces(hovertemplate=None)

        return fig
    
    def sell_bought(self):
        """Plot a car's buying year vs selling price graph."""
        
        dataframe=self.df
        fig = px.scatter(
            data_frame=dataframe.sample(30000),
            y="sellingprice",
            x="year",
            width=700,
            height=400,
            trendline="lowess",
            color="sellingprice",
        )

        fig.update_layout(xaxis_title=dict(text='<b>'"Buying Year"'</b>',
                                           font=dict(
                                           size=13)),
                          yaxis_title=dict(text='<b>'"Selling Price [$]"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Class",
                          title=dict(text="<b>Selling Price by Buying Year</b>",
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          coloraxis_colorbar_title_text = 'Selling Price',
                          hovermode="x"
        )

        fig.update_traces(hovertemplate=None)

        return fig
    
    def feats_imp(self, model):
        """Takes the model and plots the feature importances."""
        
        # get the feature importances for creating the data frame
        preds = model.model.get_feature_importance()
        feats_imp_df = pd.DataFrame(preds, index=["Buying Year", "Manufacturer", "Body Type", "State of Car", "Car's Condition", "Odometer", "Car's Paint", "MMR", "Car's Age"]).sort_values(by=0)
        
        # get the plot by using the data frame from previous step
        fig = px.bar(
            data_frame=feats_imp_df,
            width=700,
            height=400,
            orientation="h"
        )

        fig.update_layout(yaxis_title=dict(text='<b>'"Feature"'</b>',
                                           font=dict(
                                           size=13)),
                          xaxis_title=dict(text='<b>'"Importance [%]"'</b>',
                                           font=dict(
                                           size=13)),
                          legend_title_text="Paint",
                          title=dict(text="<b>Feature Importances</b>",
                                     x=0.5,
                                     y=0.95,
                                     font=dict(
                                        size=14,
                                        color='#000000'
                                     )),
                          hovermode="y"
        )
        
        # set the hover template to `None` and disable the legend
        fig.update_traces(hovertemplate=None, showlegend=False)

        return fig