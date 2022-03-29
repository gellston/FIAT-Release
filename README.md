<img src="https://github.com/gellston/FIAT-Release/blob/main/snapshoot/icons8_price_tag_96px.png?raw=true" width=40 height=40></img>
FIAT 0.6 (Fast Image Annotation Tool)
=======================

FIAT is a free image labeling tool developed in C# WPF based on Visual Studio 2022 <br/>
The current version supports labeling classification datasets and provides a PyTorch dataset loader.

Development Environment
=======================
 - **Visual Studio 2022**
 - **Microsoft .NET 6**


Download
=======================

- <a href="https://github.com/gellston/FIAT-Release/releases/download/0.6/FIAT.exe" target="_blank">FIAT 0.6 download</a>
- <a href="https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.2-windows-x64-installer" target="_blank">.NET6 framework</a>

Reference
=======================
- <a href="https://github.com/gellston/FIAT/tree/main/example_dataset" target="_blank">FIAT dataset example</a>
- <a href="https://github.com/gellston/FIAT/blob/main/python/torch_classification_FIATC_test.py" target="_blank">PyTorch training loop example (classification)</a>

DEMO
=======================
- Classification
<center>
<img src="https://github.com/gellston/FIAT-Release/blob/main/snapshoot/FIAT-example.gif?raw=true"></img>
</center>

Menu
=======================
<center>
<img src="https://github.com/gellston/FIAT-Release/blob/0.7/snapshoot/how%20to%20use%20and%20shortcut%20key.jpg?raw=true"></img>
</center>

| No | Function | No | Function |
|---|---|---|---|
| ***1*** | ***Open image folder*** | ***2*** | ***Save dataset*** |
| ***3*** | ***Add target label*** | ***4*** | ***Delete target label*** |
| ***5*** | ***Add label*** | ***6*** | ***Delete label*** |
| ***7*** | ***Add label on all*** | ***8*** | ***Delete label on all*** |
| ***9*** | ***Previous image*** | ***10*** | ***Nex image*** |
| ***11*** | ***Progress bar*** |  |  |

Shortcut Key
=======================
| Shortcut Key | Function |
|---|---|
| <kbd>F1</kbd> ~ <kbd>F12</kbd> | ***Label the image with the target label at that index*** |
| <kbd>Ctrl</kbd> + <kbd>S</kbd> | ***Save all label information*** |
| <kbd>Ctrl</kbd> + <kbd>O</kbd> | ***Open image folder*** |
| <kbd>Up</kbd> | ***Previous image*** |
| <kbd>Down</kbd> | ***Next image***  |

PyTorch training loop example
=======================
``` python
import torch
import torch.nn as nn

from torch.utils.data import DataLoader

from util.FIATClassificationDataset import FIATClassificationDataset


batch_size = 1
training_epochs = 1

datasets = FIATClassificationDataset('C://Github//FIAT//example_dataset//food//',   #FIAT dataset path
                                     label_height=224,  #image height
                                     label_width=224,   #image width
                                     isColor=True,      #color load flag
                                     isNorm=False)      #0~1 normalization flag

data_loader = DataLoader(datasets, batch_size=batch_size, shuffle=True)

for epoch in range(training_epochs):
    avg_cost = 0
    avg_acc = 0
    total_batch = len(data_loader)

    for x_input, y_input in data_loader:
        print('x_input shape = ', x_input.shape)
        print('y_input shape = ', y_input.shape)

print('Training loop finished')

```
``` console
C:\Python\python.exe C:/Github/FIAT/python/torch_classification_FIATC_test.py
{'Color': '#FFFF0000', 'Name': 'Bread'}
{'Color': '#FF008000', 'Name': 'Pizza'}
{'Color': '#FFFFFFFF', 'Name': 'Hamburger'}
{'Color': '#FFF79646', 'Name': 'Chicken'}
x_input shape =  torch.Size([1, 3, 224, 224])
y_input shape =  torch.Size([1, 4])
x_input shape =  torch.Size([1, 3, 224, 224])
y_input shape =  torch.Size([1, 4])
```


Strcture
=======================
### Classification
<img src="https://github.com/gellston/FIAT-Release/blob/main/snapshoot/snapshot1.jpg?raw=true"></img>

- __target_info.json 
    - File containing representative label information
```json
[
    {
        "Color":"#FFFF0000",
        "Name":"Bread"
        
    },
    {
        "Color":"#FF008000",
        "Name":"Pizza"
        
    },
    {
        "Color":"#FFFFFFFF",
        "Name":"Hamburger"
        
    },
    {
        "Color":"#FFF79646",
        "Name":"Chicken"
        
    }
]
```

- (each file).json 
    - A file containing user-labeled information about an image.
```json
{
    "FileName":"1_1_bread.jpg",
    "FilePath":"C:\\Users\\Fiat\\Desktop\\food\\1_1_bread.jpg",
    "ClassCollection":[
        {
            "Color":"#FFFF0000",
            "Name":"Bread"
            
        }
    ]
    
}
```




<div style="text-align: right; margin-right:30px;"> 

[TOP](#vision-studio) 

</div>

```
The MIT License (MIT)

Copyright (c) 2022-present FIAT Development Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
<div style="text-align: right; margin-right:30px;"> 

[TOP](#vision-studio) 

</div>