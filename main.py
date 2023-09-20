import matplotlib.pyplot as plt

def read_data(filename):
    fh = open(filename, "r")
    ind = 0
    lines = fh.readlines()
    for i, line in enumerate(lines):
        if "#DATA" in line:
            ind = i + 1
    x_arr = []
    y_arr = []
    for i in range(ind, len(lines)):
        x, y = lines[i].split('\t')
        x_arr.append(float(x))
        y_arr.append(float(y.replace('\n','')))
    fh.close()
    return x_arr, y_arr

def plot_data(title, x_data, y_data, filename, stype, show=False, grid=True, dpi=300):
    fig, ax = plt.subplots(figsize=(16, 9))
    fig.suptitle(title)
    ax.grid(grid)
    if stype == "IR":
        ax.invert_xaxis()
        ax.set_ylabel("Transmittance[%]")
        ax.set_xlabel(r"Wavenumber [$cm^-1$]")
    elif stype == "UV":
        ax.set_ylim(0, 1)
        ax.set_ylabel("Absorbance")
        ax.set_xlabel("Wavelength [nm]")
    ax.plot(x_data, y_data)
    plt.savefig(filename, dpi=dpi)
    if show:
        plt.show()
# Read the data from the files
x_ono, y_ono = read_data("IR/002_ono.asc")
x_no2, y_no2 = read_data("IR/002_no2.asc")
x_UV_no2, y_UV_no2 = read_data("UV/22MS003_NO2.asc")
x_UV_ono, y_UV_ono = read_data("UV/22MS003_ono.asc")
x_UV_cl, y_UV_cl = read_data("UV/22MS003_Cl.asc")

# Plot and save them. The filname should have an extension like "jpg, pdf, etc"
plot_data(title = "FT-IR spectra for $[Co(NH_3)_5ONO]Cl_2$", x_data = x_ono, y_data = y_ono, filename="ono_ir.pdf", stype="IR")
plot_data(title = "FT-IR spectra for $[Co(NH_3)_5NO_2]Cl_2$", x_data = x_no2, y_data = y_no2, filename="no2_ir.pdf", stype="IR")
plot_data(title = "UV-Vis spectra for $[Co(NH_3)_5NO_2]Cl_2$", x_data = x_UV_no2, y_data = y_UV_no2, filename="no2_uv.pdf", stype="UV")
plot_data(title = "UV-Vis spectra for $[Co(NH_3)_5ONO]Cl_2$", x_data = x_UV_ono, y_data = y_UV_ono, filename="ono_uv.pdf", stype="UV")
plot_data(title = "UV-Vis spectra for $[Co(NH_3)_5Cl]Cl_2$", x_data = x_UV_cl, y_data = y_UV_cl, filename="cl_uv.pdf", stype="UV")
