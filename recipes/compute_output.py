# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
country_economic_indicators = dataiku.Dataset("country_economic_indicators")
country_economic_indicators_df = country_economic_indicators.get_dataframe()

# MY CHANGES!!!

# Write recipe outputs
output = dataiku.Dataset("output")
output.write_with_schema(country_economic_indicators_df)
