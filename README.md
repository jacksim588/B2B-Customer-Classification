# B2B-Customer-Classification

This project Aims to use data about a buisnesses current clients, to train a model to recoginse potential future clients

An Alpha run was undertaken which used live data from Stanford Marsh, a (3D) printing company. They provided client data, and we provided the model's output.

At the moment, the feature set includes: 
- TurnoverY0
- AssetsY0
- AdminCostsY0
- Turnover%change
- Turnover/Employee
- StaffCostsPerEmployee
- TurnoverPerAdmin

We want to test features such as '# of patents', and social features; although accessing this data is difficult, and so financial data available through XBRL mining was used.

#Results:

Alpha run of Customer Classification:
- trained with limited (798) data points (399 customers, 399 random companies)
- used Random Forest Method
- Selected 114 of 128 companies ran through (companies already selected by their industry)


Confusion Matrix:

 [[48  1]
 [ 2 47]] 

True Positive Rate 96.0 %
True Negative Rate 97.92 %
Positive Predictive Value 97.96 %
Negative Predictive Value 95.92 %
False Positive Rate 2.08 %
False Negative Rate 4.0 %
False Discovery Rate 2.04 %
Overall Accuracy 96.94 %
