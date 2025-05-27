import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    def __init__(self, R=1, w=0.2, n=50):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self.compute_mesh()

    def compute_mesh(self):
        u = self.U
        v = self.V
        R = self.R
        X = (R + v * np.cos(u / 2)) * np.cos(u)
        Y = (R + v * np.cos(u / 2)) * np.sin(u)
        Z = v * np.sin(u / 2)
        return X, Y, Z

    def compute_surface_area(self):
        du = 2 * np.pi / (self.n - 1)
        dv = self.w / (self.n - 1)
        r_u_x = - (self.R + self.V * np.cos(self.U / 2)) * np.sin(self.U) - self.V * np.sin(self.U / 2) / 2 * np.cos(self.U)
        r_u_y = (self.R + self.V * np.cos(self.U / 2)) * np.cos(self.U) - self.V * np.sin(self.U / 2) / 2 * np.sin(self.U)
        r_u_z = self.V * np.cos(self.U / 2) / 2

        r_v_x = np.cos(self.U / 2) * np.cos(self.U)
        r_v_y = np.cos(self.U / 2) * np.sin(self.U)
        r_v_z = np.sin(self.U / 2)

        cross_x = r_u_y * r_v_z - r_u_z * r_v_y
        cross_y = r_u_z * r_v_x - r_u_x * r_v_z
        cross_z = r_u_x * r_v_y - r_u_y * r_v_x
        area_element = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        surface_area = np.sum(area_element) * du * dv
        return surface_area

    def compute_edge_length(self):
        x_edge = self.X[0, :]
        y_edge = self.Y[0, :]
        z_edge = self.Z[0, :]
        dx = np.diff(x_edge)
        dy = np.diff(y_edge)
        dz = np.diff(z_edge)
        segment_lengths = np.sqrt(dx**2 + dy**2 + dz**2)
        return np.sum(segment_lengths)

    def plot(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, color='skyblue', edgecolor='gray', alpha=0.9)
        ax.set_title('Möbius Strip')
        plt.tight_layout()
        plt.show()

# Beginner-friendly execution
mobius = MobiusStrip(R=1, w=0.4, n=30)
area = mobius.compute_surface_area()
length = mobius.compute_edge_length()
mobius.plot()
area, length
