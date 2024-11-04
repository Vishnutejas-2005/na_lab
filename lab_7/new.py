def sim_dict():
  # For now, We have made the Filters sim_dict only. From the given data, the Filters field was used only to group the data
  filters_dict_with_given_prompts = {
    ("iss_bin","issuer bin","bin","id number","bank id num","bank id"):"iss_bin",
    ("mcc","merchant category code"):"mcc",                                                                          #check with r.mcc
    ("merchant names","merchant",):"merchant_name",
    ("reasoncode","error code","reasons","decline reasons"):"reason_code",
    ("credit card","debit card","card","card type","cc","dc","cc flag","dc flag"):"cc_dc_flag",
    ("variant","card variant","classic","platinum"):"card_variant",
    ("channel type","channel"):"channeltype",
    ("approved transactions","declined transactions","approved","declined","approval","approve_decline_flag"):"approve_decline_flag",
    ("Bank of India","issuing bank","issuing bankwise"):"iss_bankname",
    ("acquirer bank","Bank of India"):"acq_bankname",
    ("reasoncodedesc","decription of errors","descriptions","reasons"):"reasoncodedesc",
    ("mcc description"):"mcc_desc",
    ("amount","amt","transaction value","value","transactions","total amount","spend"):"amt", 
  }
  filters_dict_with_no_examples = {
    ():"rrn",
    ():"asdt",
    ():"iss_participant_id",          
    ():"acq_bin",                     
    ():"acq_participant_id",          
    ():"location_card",
    ():"merchant_id",
    ():"pincode",
    ():"state",
    ():"iss_bnkcd",
    ():"acq_bnkcd",
    ():"terminal_id",
    ():"cashatpos_flag",
    ():"func_code_desc",
    ():"transaction_type",
    ():"pan",
  }