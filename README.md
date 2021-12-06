1. Given a list of withdrawals and deposits that have occured at various exchanges in our accounts in the csv file.
2. Match up withdrawls with their corresponding deposits to create a complete history of transfers. The matched pair is a complete 'transfer' record from one exchange to another.
3. Flag any unmatched deposits or withdrawals that might have experienced a transfer error and thus no corresponding record exists for them.
4. Flag any transfer that started before 8am and finished after 8am.
5. Some withdrawals could have been aggregated and transferred in a group, appearing as an aggregate amount in the deposit record on the other side.
