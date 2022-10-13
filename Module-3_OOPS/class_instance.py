class student:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)


# Calling via Object
"""st=student()
st.getdata()
st.stid=23
st.stnm='Ashok'
st.getdata()"""

# Calling via Instance
student().getdata()
student().stid=12
student().stnm='Sanket'
student().getdata()