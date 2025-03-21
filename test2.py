# coding: utf-8
import matplotlib.pyplot as plt
from astropy import units as u
plt.ion()
b = [12, 26, 69] * u.second
c = [42, 57, 66] * u.meter
plt.plot(b, c, 'og', ls='')
plt.xlabel("seconds")
plt.ylabel("meters")
plt.savefig('test2.png')
print("Done! Figure saved.")
