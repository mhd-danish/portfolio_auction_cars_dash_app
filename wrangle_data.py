# This file loads the data and then cleans it for exploratory data analysis

import pandas as pd  # for manipulating the dataset
import numpy as np  # scientific computing
import warnings  # for filtering all kinds of warnings: NOT RECOMMENDED
warnings.filterwarnings("ignore")


class Data:
    """Accepts the data path and loads the data and also performs wrangling on the dataset that will be used for EDA and machine learning."""
    
    def __init__(self, path="./dataset/car_prices.csv"):
        
        self.path = path # get the path to the dataframe
        self.data = pd.read_csv(self.path, header=0, error_bad_lines=False, warn_bad_lines=False)  # import the data

    def __clean_make(self):
        """lowers the string case and performs wrangling on `make` feature to improve consistency."""

        self.data["make"] = self.data.make.str.lower()
        self.data["make"] = self.data.make.replace("chev truck", "chevrolet")
        self.data["make"] = self.data.make.replace("chev truck", "chevrolet")
        self.data["make"] = self.data.make.replace("mazda tk", "mazda")
        self.data["make"] = self.data.make.replace("vw", "volkswagen")
        self.data["make"] = self.data.make.replace(["ford tk", "ford truck"], "ford")
        self.data["make"] = self.data.make.replace("dodge tk", "dodge")
        self.data["make"] = self.data.make.replace("hyundai tk", "hyundai")
        self.data["make"] = self.data.make.replace("gmc truck", "gmc")
        self.data["make"] = self.data.make.replace(["mercedes-b", "mercedes-benz"], "mercedes")

        return self.data

    def __clean_body(self):
        """lowers the string case and performs wrangling on `body` feature to improve consistency."""

        self.data["body"] = self.data.body.str.lower()
        for x in self.data.body.unique().tolist():
            if "sedan" in str(x):
                self.data["body"] = self.data.body.replace(str(x), "sedan")

        for x in self.data.body.unique().tolist():
            if "coupe" in str(x):
                self.data["body"] = self.data.body.replace(str(x), "coupe")

        for x in self.data.body.unique().tolist():
            if "cab" in str(x):
                self.data["body"] = self.data.body.replace(str(x), "cab")

        for x in self.data.body.unique().tolist():
            if "convertible" in str(x):
                self.data["body"] = self.data.body.replace(str(x), "convertible")

        for x in self.data.body.unique().tolist():
            if "wagon" in str(x):
                self.data["body"] = self.data.body.replace(str(x), "wagon")

        for x in self.data.body.unique().tolist():
            if "van" in str(x):
                self.data["body"] = self.data.body.replace(str(x), "van")

        return self.data

    def __clean_color(self):
        """performs wrangling on `color` feature to improve consistency."""
        
        # replace `-` with `other` in the `color` feature
        self.data["color"] = self.data.color.replace("—", "other")

        return self.data


    def wrangle(self):
        """Accepts the data path and loads the data and also performs wrangling on the dataset that will be used for EDA and machine learning."""

        # change the saledate to have datetime format
        self.data.loc[:, "saledate"] = pd.to_datetime(self.data.saledate, utc=True).dt.year
        
        
        # feature engineering on saledate
        self.data["age_when_sold"] = self.data["saledate"] - self.data["year"]
        self.data.loc[self.data["age_when_sold"].lt(0), "age_when_sold"] = 0


        # drop columns that are useless or have high cardinality
        self.data.drop(["saledate", "seller", "vin"], axis=1, inplace=True)

        # dropping features with low importances
        self.data.drop(["transmission", "model", "trim", "interior"], axis=1, inplace=True)

        # drop records
        self.data.dropna(subset=["body"], how="all", inplace=True)
        self.data.dropna(subset=["color"], how="all", inplace=True)
        self.data.dropna(subset=["condition"], how="all", inplace=True)

        # lower and replace misspellings all the string values for consistency
        self.data = self.__clean_make()
        self.data = self.__clean_body()
        self.data = self.__clean_color()

        # take absolute of odometer
        self.data["odometer"] = self.data.odometer.apply(lambda x: x if x>=0 else 0)

        # take absolute of odometer
        self.data["sellingprice"] = self.data.sellingprice.apply(lambda x: x if x>=0 else 0)

        # getting rid of outliers in odometer feature
        self.data = self.data[self.data.odometer.le(self.data.odometer.quantile(0.99))]


        return self.data