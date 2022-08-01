import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


def coc_f():
    """
    x: Focal length
    y: Distance
    z: Circle of confusion
    """

    n = 2      # f-numbers (Aperture)
    s = 1000   # Object (focus) distance (mm)

    F = np.arange(1, 50, 0.1)  # Focal length (mm)
    D = np.arange(500, 5000, 100)  # Distance (mm)

    C = np.array([[f/(s-f)*f/n*abs(s-d)/d for f in F] for d in D])  # Circle of confusion (CoC) (mm)

    cs = plt.contourf(F, D, C, levels=100)
    cs2 = plt.contour(F, D, C, levels=[0.029], colors='orange')
    cs2.collections[0].set_label('0.029')
    plt.legend(loc='upper left')

    cbar = plt.colorbar(cs)
    cbar.set_label('Circle of Confusion Size')

    plt.xlabel('Focal length (mm)')
    plt.ylabel('Distance (mm)')

    plt.title(f'Object: {s/1000}m, Aperture: f/{n}')
    plt.show()

def coc_f_m():
    """
    x: Focal length
    y: Distance
    z: Magnification
    """

    n = 2      # f-numbers (Aperture)
    s = 1000   # Object (focus) distance (mm)

    F = np.arange(1, 50, 0.1)  # Focal length (mm)
    D = np.arange(500, 5000, 100)  # Distance (mm)

    M = np.array([[s*f/(s-f)/d for f in F] for d in D])  # Magnification

    cs = plt.contourf(F, D, M, levels=100)

    cbar = plt.colorbar(cs)
    cbar.set_label('Magnification')

    plt.xlabel('Focal length (mm)')
    plt.ylabel('Distance (mm)')

    plt.title(f'Object: {s/1000}m, Aperture: f/{n}')
    plt.show()

def coc_a():
    """
    x: f-numbers
    y: Distance
    z: Circle of confusion
    """

    s = 1000   # Object (focus) distance (mm)
    f = 35     # Focal length (mm)

    N = np.arange(1, 30, 0.1)  # f-numbers (Aperture)
    # N = np.array([np.around(np.power(2, 0.5*i), 1) for i in range(10)])  # f-numbers (Aperture) (practial)
    D = np.arange(500, 5000, 100)  # Distance (mm)

    C = np.array([[f/(s-f)*f/n*abs(s-d)/d for n in N] for d in D])  # Circle of confusion (CoC) (mm)

    cs = plt.contourf(N, D, C, levels=100)
    cs2 = plt.contour(N, D, C, levels=[0.029], colors='orange')
    cs2.collections[0].set_label('0.029')
    plt.legend(loc='upper left')

    cbar = plt.colorbar(cs)
    cbar.set_label('Circle of Confusion Size')

    plt.xscale('log')
    plt.xticks([np.floor(np.power(2, 0.5*i)*10)/10 for i in range(10)])
    plt.minorticks_off()

    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('f/{x:.1f}'))

    plt.xlabel('Aperture')
    plt.ylabel('Distance (mm)')

    plt.title(f'Object: {s/1000}m, Focal length: {f}mm')
    plt.suptitle('CoC')
    plt.show()

def coc_s():
    """
    x: Focus distance
    y: Distance
    z: Circle of confusion
    """

    n = 2  # f-numbers (Aperture)
    f = 35  # Focal length (mm)

    S = np.arange(1000, 5000, 10)  # Distance (mm)
    D = np.arange(800, 10000, 10)  # Distance (mm)

    # h = f+f*f/n/0.029  # Hyperfocal distance (mm)
    # S = np.linspace(1000, 23000, 100)
    # D = np.linspace(1000, 100000, 1000)
    # plt.plot([h for _ in D], D, color='r', label='Hyperfocal')

    C = np.array([[f/(s-f)*f/n*abs(s-d)/d for s in S] for d in D])  # Circle of confusion (CoC) (mm)

    cs = plt.contourf(S, D, C, levels=100)
    cs2 = plt.contour(S, D, C, levels=[0.029], colors='orange')
    cs2.collections[0].set_label('0.029')

    plt.legend(loc='upper left')

    cbar = plt.colorbar(cs)
    cbar.set_label('Circle of Confusion Size')

    plt.xlabel('Object Distance (mm)')
    plt.ylabel('Distance (mm)')

    plt.title(f'Focal length: {f}mm, Aperture: f/{n}')
    plt.show()

def coc_s_m():
    """
    x: f-numbers
    y: Distance
    z: Magnification
    """

    n = 2  # f-numbers (Aperture)
    f = 35     # Focal length (mm)

    S = np.arange(100, 2000, 10)  # Distance (mm)
    D = np.arange(1000, 2000, 10)  # Distance (mm)

    M = np.array([[s*f/(s-f)/d for s in S] for d in D])  # Magnification

    cs = plt.contourf(S, D, M, levels=100)

    cbar = plt.colorbar(cs)
    cbar.set_label('Magnification')

    plt.xlabel('Object Distance (mm)')
    plt.ylabel('Distance (mm)')

    plt.title(f'Focal length: {f}mm, Aperture: f/{n}')
    plt.show()


def mag(relative=True):
    """
    x: Focal length
    y: Distance
    z: Magnification
    """

    m0 = 0.005   # Object Magnification (m = f/(s-f), s = (m+1/m)f)

    F = np.arange(10, 100, 10)
    D = np.arange(1000, 50000, 1000)

    if relative:
        # Relative distance to object
        M = np.array([[(m0+1)*f/(d+(m0+1)/m0*f) for f in F] for d in D])
        cs = plt.contourf(F, D, M, 20)
        plt.ylabel('Relative Distance (mm)')
    else:
        M = np.array([[(m0+1)*f/d for f in F] for d in D])

        cs = plt.contourf(F, D, M, levels=[m0+m0*(i-10)*0.1 for i in range(40)])
        plt.plot(F, (m0+1)/m0*F, color='red', label='object')
        plt.legend()
        plt.ylabel('Distance (mm)')

    plt.xlabel('Focal length (mm)')
    # plt.clabel(cs)
    plt.title('Magnification')
    plt.colorbar(cs)
    plt.show()


def dof(var, fixed='s'):
    """ calculate Depth of Field
        var: f, N, s, m
        fixed: s, m
    """

    c = 0.029  # Circle of confusion (CoC) (mm)
    f = 50     # Focal length (mm)
    N = 2      # f-numbers (Aperture)
    s = 1000   # Object distance (mm)
    m = 0.05   # Magnification (m = f/(s-f), s = (m+1/m)f)

    if var == 'f':
        fig, ax = plt.subplots()
        ax2 = ax.twinx()
        f = np.arange(1, 50, 0.1)

        if fixed == 's':
            m = f/(s-f)
            ax.plot(f, [s for _ in f], label='Object')
            ax2.plot(f, m, label='Magnification', color='orange')
            ax.set_ylim(0, 5*s)

        elif fixed == 'm':
            s = (m+1)/m*f
            ax.plot(f, s, label='Object')
            ax2.plot(f, [m for _ in f], label='Magnification', color='orange')

        df = s*f*f/(f*f + N*c*f - N*c*s)
        dn = s*f*f/(f*f - N*c*f + N*c*s)

        ax.fill_between(f, df, dn, alpha=.3)

        ax.set_xlabel('Focal length (mm)')
        ax.set_ylabel('Distance (mm)')

        ax2.set_ylabel('Magnification')

        fig.legend(bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    elif var == 'N':
        fig, ax = plt.subplots()
        N = np.arange(100)

        df = s*f*f/(f*f + N*c*f - N*c*s)
        dn = s*f*f/(f*f - N*c*f + N*c*s)

        ax.plot(N, [s for _ in N], label='Object')
        ax.fill_between(N, df, dn, alpha=.3)

        ax.set_xlabel('f-numbers')
        ax.set_ylabel('Distance (mm)')
        ax.set_ylim(0, 5*s)

        m = f/(s-f)
        ax2 = ax.twinx()

        ax2.plot(N, [m for _ in N], label='Magnification', color='orange')
        ax2.set_ylabel('Magnification')

        fig.legend(bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    elif var == 's':
        fig, ax = plt.subplots()

        s = np.arange(2*f, 10000, 100)  # s > f
        df = s*f*f/(f*f + N*c*f - N*c*s)
        dn = s*f*f/(f*f - N*c*f + N*c*s)

        ax.plot(s, s, label='Object')
        ax.fill_between(s, df, dn, alpha=.3)

        ax.set_xlabel('Object Distace (mm)')
        ax.set_ylabel('Distance (mm)')

        m = f/(s-f)
        ax2 = ax.twinx()
        ax2.plot(s, m, label='Magnification', color='orange')
        ax2.set_ylabel('Magnification')

        fig.legend(bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    elif var == 'm':
        fig, ax = plt.subplots()

        m = np.arange(0, 0.1, 0.01)
        s = (m+1)/m*f

        df = s*f*f/(f*f + N*c*f - N*c*s)
        dn = s*f*f/(f*f - N*c*f + N*c*s)

        ax.plot(m, s, label='Object')
        ax.fill_between(m, df, dn, alpha=.3)

        ax.set_xlabel('Magnification')
        ax.set_ylabel('Distance (mm)')

        ax2 = ax.twinx()
        ax2.plot(m, m, label='Magnification', color='orange')
        ax2.set_ylabel('Magnification')

        fig.legend(bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)

    plt.title('Depth of Field')
    plt.show()


if __name__ == '__main__':
    # dof('f', 's')
    # dof('f', 'm')
    # dof('N')
    # dof('s')
    # dof('m')

    # mag(False)
    # mag(True)

    coc_f()
    # coc_f_m()
    # coc_a()
    # coc_s()
    # coc_s_m()
