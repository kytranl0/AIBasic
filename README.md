
Source: 
https://github.com/aimacode/aima-java
pip install pandas
pip install matplotlib
pip install torch
pip install seaborn


Data:
"Time","V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount","Class"


0,-1.3598071336738,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.0986979012610507,0.363786969611213,0.0907941719789316,-0.551599533260813,-0.617800855762348,-0.991389847235408,-0.311169353699879,1.46817697209427,-0.470400525259478,0.207971241929242,0.0257905801985591,0.403992960255733,0.251412098239705,-0.018306777944153,0.277837575558899,-0.110473910188767,0.0669280749146731,0.128539358273528,-0.189114843888824,0.133558376740387,-0.0210530534538215,149.62,"0"

Understanding the data:
    The dataset has been anonymised and many attributes (features) have been removed.
    Features (attributes) have been labelled as V1, V2,..and only numerical data is included
    (PCA) Principal Component Analysis already applied to this dataset
        Only features not transformed with PCA are ‘Time’ and ‘Amount’
        ‘Time’ contains the seconds elapsed between each transaction and the first transaction in the dataset
        The feature ‘Amount’ is the transaction Amount, this feature can be used for example-dependant cost-senstive learning
        Feature ‘Class’ is the response variable and it takes value 1 in case of fraud and 0 otherwise.


Autoencoders - are artificial neural networks capable of learning efficient representations of the input data. This learned representation is called ‘coding’ and this learning happens unsupervised
    *encoder*(recognition network) which is responsible for converting the inputs to an internal representation. Encoder is followed by a *decoder* (generative network) that converts the internal representation to the outputs.