{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "00fede80-7e7a-426f-b077-e5b496e00e0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SBI Small Cap Fund - Direct Plan - Growth\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>nav</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>22-06-2026</td>\n",
       "      <td>204.12630</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>19-06-2026</td>\n",
       "      <td>202.07610</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>18-06-2026</td>\n",
       "      <td>200.95650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>17-06-2026</td>\n",
       "      <td>199.83020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>16-06-2026</td>\n",
       "      <td>198.61520</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         date        nav\n",
       "0  22-06-2026  204.12630\n",
       "1  19-06-2026  202.07610\n",
       "2  18-06-2026  200.95650\n",
       "3  17-06-2026  199.83020\n",
       "4  16-06-2026  198.61520"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "url = \"https://api.mfapi.in/mf/125497\"\n",
    "\n",
    "response = requests.get(url)\n",
    "\n",
    "data = response.json()\n",
    "\n",
    "print(data[\"meta\"][\"scheme_name\"])\n",
    "\n",
    "nav_df = pd.DataFrame(data[\"data\"])\n",
    "\n",
    "nav_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ac36e3d2-561a-4937-b1f2-a7b2ffc17f86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved\n"
     ]
    }
   ],
   "source": [
    "nav_df.to_csv(\n",
    "    r\"E:\\Project\\data\\raw\\hdfc_top100_nav.csv\",\n",
    "    index=False\n",
    ")\n",
    "\n",
    "print(\"Saved\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f539537f-6d5f-464a-99ee-ef3bbe11dae4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SBI_Bluechip saved\n",
      "ICICI_Bluechip saved\n",
      "Nippon_LargeCap saved\n",
      "Axis_Bluechip saved\n",
      "Kotak_Bluechip saved\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "schemes = {\n",
    "    \"SBI_Bluechip\":119551,\n",
    "    \"ICICI_Bluechip\":120503,\n",
    "    \"Nippon_LargeCap\":118632,\n",
    "    \"Axis_Bluechip\":119092,\n",
    "    \"Kotak_Bluechip\":120841\n",
    "}\n",
    "\n",
    "for name,code in schemes.items():\n",
    "\n",
    "    url = f\"https://api.mfapi.in/mf/{code}\"\n",
    "\n",
    "    data = requests.get(url).json()\n",
    "\n",
    "    df = pd.DataFrame(data[\"data\"])\n",
    "\n",
    "    df.to_csv(\n",
    "        rf\"E:\\Project\\data\\raw\\{name}.csv\",\n",
    "        index=False\n",
    "    )\n",
    "\n",
    "    print(f\"{name} saved\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b6072f19-d362-4193-9a1d-f9c8133ae49d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (40, 15)\n",
      "\n",
      "Columns:\n",
      "['amfi_code', 'fund_house', 'scheme_name', 'category', 'sub_category', 'plan', 'launch_date', 'benchmark', 'expense_ratio_pct', 'exit_load_pct', 'min_sip_amount', 'min_lumpsum_amount', 'fund_manager', 'risk_category', 'sebi_category_code']\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "fund_master = pd.read_csv(r\"E:\\Project\\data\\raw\\01_fund_master.csv\")\n",
    "\n",
    "print(\"Shape:\", fund_master.shape)\n",
    "\n",
    "print(\"\\nColumns:\")\n",
    "print(fund_master.columns.tolist())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4867ecfc-3693-486c-a4ae-1a322820f166",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unique Fund Houses:\n",
      "10\n",
      "<ArrowStringArray>\n",
      "[         'SBI Mutual Fund',         'HDFC Mutual Fund',\n",
      "      'ICICI Prudential MF',          'Nippon India MF',\n",
      "        'Kotak Mahindra MF',         'Axis Mutual Fund',\n",
      " 'Aditya Birla Sun Life MF',          'UTI Mutual Fund',\n",
      "           'Mirae Asset MF',          'DSP Mutual Fund']\n",
      "Length: 10, dtype: str\n"
     ]
    }
   ],
   "source": [
    "print(\"Unique Fund Houses:\")\n",
    "\n",
    "print(fund_master['fund_house'].nunique())\n",
    "print(fund_master['fund_house'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dcfea18e-b62f-4518-91b9-0d9c139531ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unique Categories:\n",
      "<ArrowStringArray>\n",
      "['Equity', 'Debt']\n",
      "Length: 2, dtype: str\n"
     ]
    }
   ],
   "source": [
    "print(\"Unique Categories:\")\n",
    "print(fund_master['category'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b60f728-e730-4982-9a21-6e19e07583fb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07c32f79-5697-4b55-a5ec-860aead5c99a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
