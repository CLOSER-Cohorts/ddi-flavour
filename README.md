# ddi-flavour
Scripts to convert between SledgeHammer output and Colectica and add in some nice naming

| Edit script  | Explanation                                    |
| --- | :---|
| fandr.py     | Insert <r:String> where absent from output     |
| fandr2.py    | Names the DDI Instance                         |
| fandr3.py    | Names the Physical Instance                    |
| fandr4.py    | Names the Logical Product                      |
| fandr5.py    | Names the Code List scheme                     |
| fandr6.py    | Names the Data Product Name                    |
| fandr7.py    | Add Dataset URI and whether public             |
| fandr8.py    | Adds Title and Alternate Title to DDI Instance |
| fandr9.py    | Corrects Valid to be ValidCases                |
| fandr10.py   | Corrects Invalid to be InvalidCases            |
| fandr11.py   | Adds naming to DataRelationship                | 


Input 
- DDI dataset XML from Sledgehammer output
- Tab delimited.txt file named renaming_list.txt which should contain; the instrument prefix, dataset title, DOI/webiste link, and whehter to show the link publically (1) or not (0)
