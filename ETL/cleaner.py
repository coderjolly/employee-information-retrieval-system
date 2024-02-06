# importing required libraries
import pandas as pd
from config_class import Config

# defing a class which has methods to
class Transform:
    def __init__(self):
        self.configObj = Config()
        self.config_extracted_df = self.configObj.read_config()
        data_staging = self.configObj.get_staging(self.config_extracted_df)

    # method which accepts a dataframe and performs some transformations before returning it to next function.
    def transform_data(self, extracted_df):
        extracted_df["employee_name"] = (
            extracted_df["first_name"]
            + " "
            + extracted_df["mid_init"]
            + " "
            + extracted_df["last_name"]
        )

        extracted_df.drop(
            columns=["first_name", "last_name", "mid_init"], axis=1, inplace=True
        )
        # Renaming Columns

        extracted_df.rename(
            columns={
                "leave_status_as_of_july_31": "work_status",
                "regular_hours": "work_hours",
                "base_salary": "base_salary_USD",
                "regular_gross_paid": "gross_salary_USD",
                "ot_hours": "overtime_hours",
                "total_ot_paid": "overtime_commission_USD",
                "total_other_pay": "other_pay_USD",
            },
            inplace=True,
            errors="raise",
        )

        extracted_df["work_status"].replace(
            {"CEASED": "TERMINATED", "SEASONAL": "CONTRACTUAL"}, inplace=True
        )

        # formatting date

        extracted_df["agency_start_date"] = (
            extracted_df["agency_start_date"].str.split("T").str[0]
        )

        extracted_df = extracted_df[
            [
                "fiscal_year",
                "payroll_number",
                "agency_name",
                "agency_start_date",
                "work_location_borough",
                "employee_name",
                "title_description",
                "work_status",
                "base_salary_USD",
                "pay_basis",
                "work_hours",
                "gross_salary_USD",
                "overtime_hours",
                "overtime_commission_USD",
                "other_pay_USD",
            ]
        ]

        extracted_df = extracted_df.drop_duplicates()

        extracted_df.dropna(subset=["employee_name"], inplace=True)
        extracted_df.dropna(subset=["title_description"], inplace=True)

        extracted_df["employee_name"].astype("str").str.replace(r".", r"", regex=False)
        extracted_df["employee_name"].astype("str").str.replace(r"-", r"", regex=False)

        extracted_df.sort_values(
            ["fiscal_year", "employee_name"], ascending=[True, True], inplace=True
        )
        extracted_df["work_location_borough"] = extracted_df.groupby(["agency_name"])[
            "work_location_borough"
        ].bfill()
        extracted_df.dropna(subset=["work_location_borough"], inplace=True)

        extracted_df.drop(
            extracted_df.loc[extracted_df["employee_name"] == "xxx xxx"].index,
            inplace=True,
        )
        extracted_df.drop(
            extracted_df.loc[extracted_df["pay_basis"] == "Prorated Annual"].index,
            inplace=True,
        )

        extracted_df[["work_location_borough", "agency_name", "title_description"]] = (
            extracted_df[["work_location_borough", "agency_name", "title_description"]]
            .astype(str)
            .apply(lambda col: col.str.upper())
        )

        cols = extracted_df.select_dtypes(object).columns
        extracted_df[cols] = extracted_df[cols].apply(lambda x: x.str.strip())
        return extracted_df
