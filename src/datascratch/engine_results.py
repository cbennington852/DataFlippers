import matplotlib.pyplot as plt
import pandas as pd
import traceback
import numpy as np

class InternalEngineError(Exception):
    pass


class ModelTrainingResults():
    """
    Small class to hold the results from training the model.
    """
    def __init__(self , 
    y_predictions , 
    trained_model,
    relevant_statistical_results : list[(str , float)] # can also be an int
    ):
        self.y_predictions = y_predictions
        self.trained_model = trained_model
        self.relevant_statistical_results = relevant_statistical_results





class ConvertedColumn():
    def __init__(self , column_name , code_map):
        self.column_name = column_name
        self.code_map = code_map.tolist()

    def check_if_col_name_in_list_converted_columns(list_converted_cols : list , col_name : str):
        for converted_col in list_converted_cols:
            if converted_col.column_name == col_name:
                return converted_col
        return None

    def convert_int_to_string(self , value):
        # Regressors could feed a non-int into here.
        return self.code_map[int(value)]
    
    def convert_string_to_int(self, value):
        for x in range(0 , len(self.code_map)):
            if value == self.code_map[x]:
                return x
        raise InternalEngineError(f"{value} is not a value in the trained dataset.")
    


class EngineResults():
    """
    Small class to hold the results from the engine.
    """
    def __init__(
            self, 
            visual_plot : list[plt.Figure],
            accuracy_plot : list[plt.Figure], 
            trained_models : list , 
            x_cols : list[str] , 
            y_col : list[str],
            list_converted_columns : list,
            dataframe : pd.DataFrame,
            ):
        self.visual_plot = visual_plot
        self.accuracy_plot = accuracy_plot
        self.trained_models = trained_models
        self.x_cols = x_cols
        self.y_col = y_col
        self.list_converted_columns = list_converted_columns

        # Resolving a map of the types.
        self.column_types : dict[str , any] = dict()
        column_names = dataframe.columns
        first_row = dataframe.iloc[0].values
        for k in range(0 , len(column_names)):
            curr_value = first_row[k]
            curr_col_name = column_names[k]
            curr_type = None
            if type(curr_value) == str:
                curr_type = str
            else:
                curr_type = type(curr_value.item())
            final_val = None
            if curr_type == int:
                final_val = 0
            elif curr_type == float:
                final_val = 0.0
            elif curr_type == bool:
                final_val = False
            elif curr_type == complex:
                final_val = complex(1, 1)
            else:
                final_val = ""
            self.column_types[curr_col_name] = final_val
    def is_column_in_list_converted_columns(self, col_name : str):
        try:
            for converted_col in self.list_converted_columns:
                if col_name == converted_col.column_name:
                    return True
            return False
        except:
            return False
    def get_converted_column(self , col_name):
        for converted_col in self.list_converted_columns:
            if col_name == converted_col.column_name:
                return converted_col
        
            
    def predict_from_df(self , new_df : pd.DataFrame) -> pd.DataFrame:

        # 1. Remove nan-values
        df_na_dropped = new_df.dropna()

        # 2. Perform conversion on converted columns using converted columns.
        def convert_column(column : pd.Series): 
            converted_col = self.get_converted_column(column.name)
            if converted_col:
                # perform conversion. 
                def apply_to_rows(curr_item):
                    return converted_col.convert_string_to_int(curr_item)
                new_col = column.apply(apply_to_rows)
                return new_col
            else:
                return column

        # 3. Gather only the columns that we trained this model on. 
        converted_df = df_na_dropped.apply(convert_column)
        df_reduced = pd.DataFrame()
        for col_name in self.x_cols:
            # Check df has these col_names
            try:
                df_reduced[col_name] = converted_df[[col_name]]
            except Exception as e:
                traceback.print_exception(e)
                raise InternalEngineError(f"The Inputted dataframe column names do not match the trained dataset column names. {col_name} is missing inputted dataset.")

        # 4. Get dataframe for user
        df_shown_to_user = pd.DataFrame()
        for col_name in self.x_cols:
            df_shown_to_user[col_name] = df_na_dropped[[col_name]]

        # 5. Add each model prediction as a column.
        for pipeline in self.trained_models:
            try:
                curr_df_pred = pipeline.sklearn_pipeline.predict(df_reduced)
                # If y_col in converted col, apply the conversion function. 
                converted_col = self.get_converted_column(self.y_col[0])
                def convert_back(item):
                    return converted_col.code_map[item]
                vectorised_func = np.vectorize(convert_back)
                if converted_col:
                    curr_df_pred = vectorised_func(curr_df_pred)
                else:
                    pass
                df_shown_to_user[f"{self.y_col[0]}_{pipeline.name}"] = curr_df_pred
            except Exception as e:
                traceback.print_exception(e)
                raise InternalEngineError(f"Model Training error. {str(e)}")

        print("Model Preds" , df_shown_to_user)
        return df_shown_to_user
        
    

    def predict(self , x_values : list ):
        if len(self.x_cols) != len(x_values):
            raise InternalEngineError("Did not provide all of the values. Must provide all values.")
       
        # Resolve the list of converted columns.
        for converted_col in self.list_converted_columns:
            for j in range(0 ,len(self.x_cols)):
                if converted_col.column_name == self.x_cols[j]:
                    x_values[j] = converted_col.convert_string_to_int(x_values[j])
                    # Convert thing

                    
        # Assemble as dataframe
        tmp_df = pd.DataFrame([x_values] , columns=self.x_cols)
        results = {}
        for pipeline in self.trained_models:
            curr = pipeline.predict(tmp_df)
            if self.list_converted_columns != []:
                for converted_col in self.list_converted_columns:
                    if self.y_col[0] == converted_col.column_name:
                        # Perform an int conversion because someone could "theoretically" put in a non int here.
                        results[pipeline] = converted_col.convert_int_to_string(curr)
                    else:
                        results[pipeline] = curr
            else:
                results[pipeline] = curr
        return results