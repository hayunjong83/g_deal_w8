from pyhwpx import Hwp
hwpx = Hwp()
# hwpx.register_module(
#   "FilePathCheckDLL", 
#   "HwpAutomationModule")

file_name="frame"
hwpx.open(file_name + ".hwp")

phone_nums = ["000-0000-0000",
              "111-1111-1111",
              "222-2222-2222"]

for i, phone in enumerate(phone_nums):
  # print(i)
  # print(phone)
  hwpx.put_field_text("phone", phone)
  hwpx.save_as(file_name+"_i.hwp")

hwpx.Quit()



# hwpx.put_field_text("phone", "000-0000-0000")
# hwpx.save_as(hwpx.Path.replace(
#   ".hwp", "_hayunjong.hwp"))
# hwpx.Quit()