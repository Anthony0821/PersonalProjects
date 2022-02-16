using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;
namespace BankingInterface
{
    public partial class Form1 : Form
    {
        [DllImport("Gdi32.dll", EntryPoint = "CreateRoundRectRgn")]

        private static extern IntPtr CreateRoundRectRgn
            (
            int nLeftRect,
            int nToprect,
            int nRightRect,
            int nBottomRect,
            int nWidthEllipse,
            int nHeightEllipse
            );


        public Form1()
        {
            InitializeComponent();
            Region = System.Drawing.Region.FromHrgn(CreateRoundRectRgn(0, 0, Width, Height, 25, 25));
            PNLNav.Height = BtnProfile.Height;
            PNLNav.Top = BtnProfile.Top;
            PNLNav.Left = BtnProfile.Left;
            BtnProfile.BackColor = Color.FromArgb(46, 51, 73);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void BtnProfile_Click(object sender, EventArgs e)
        {
            PNLNav.Height = BtnProfile.Height;
            PNLNav.Top = BtnProfile.Top;
            PNLNav.Left = BtnProfile.Left;
            BtnProfile.BackColor = Color.FromArgb(46, 51, 73);
        }
    }
}
