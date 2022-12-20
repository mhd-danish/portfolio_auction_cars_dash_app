# This script trains a catboost regressor model and makes a prediction

from sklearn.model_selection import train_test_split # for splitting the dataset into traning and validation datasets
from catboost import CatBoostRegressor, Pool  # Tree Model
import joblib  # for saving and loading the model
import wrangle_data  # used for getting dataset either raw or wrangled
import datetime  # for getting current datetime
import glob  # for getting the path of the saved model
import warnings  #  using it to ignore any type of warnings: NOT RECOMMENDED!
warnings.filterwarnings("ignore")

class Model:
    """Takes the wrangled data for training, saving and loading the model."""
    def __init__(self, training=False):
        
        self.__training = False  # ignore it
    
    def train_and_save(self):
        """Trains and saves the model."""
        
        # wrangle the data
        self.df = wrangle_data.Data().wrangle()
        
        # get the target labels
        y = self.df.sellingprice
        
        # get the features
        X = self.df.drop("sellingprice", axis=1)
        
        # splitting the original dataset for getting training and testing data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.1, random_state=42)
        
        # Pool the evaluation dataset
        eval_set = Pool(self.X_test, self.y_test, cat_features=self.df.select_dtypes("object").columns.tolist())
        
        # initialize the CatBoostClassifier as `imputer` and fit the training data
        self.model = CatBoostRegressor(cat_features=self.df.select_dtypes("object").columns.tolist())
        
        # now fit the data
        self.model.fit(self.X_train, self.y_train, eval_set=eval_set, verbose=True)
        
        print("Model Trained!")
        
        # save the model
        joblib.dump(self.model, f"../OneDrive/Desktop/Portfolio/Auction Cars/saved_models/model_{datetime.datetime.now().day}{datetime.datetime.now().minute}.pkl")
        
        print("Model Saved!")
        
    
    def load(self):
        """Loads a latest pre-trained saved model from storage."""
        # Try to load the model. If no model is saved previously then print the message
        try:
            self.model = joblib.load(sorted(glob.glob("saved_models/*"))[-1])
        except:
            print("Check if there is a trained model")
        
    def predict(self, X_test):
        """Takes the testing data and exports the predictions."""
        
        # get the prediction
        preds = self.model.predict(X_test)
        
        return preds