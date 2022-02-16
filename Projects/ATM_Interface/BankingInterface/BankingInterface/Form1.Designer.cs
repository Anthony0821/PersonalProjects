
namespace BankingInterface
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.User = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.BtnProfile = new System.Windows.Forms.Button();
            this.BtnAccountBalance = new System.Windows.Forms.Button();
            this.BtnLogout = new System.Windows.Forms.Button();
            this.BtnStatements = new System.Windows.Forms.Button();
            this.BtnSatistics = new System.Windows.Forms.Button();
            this.PNLNav = new System.Windows.Forms.Panel();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(24)))), ((int)(((byte)(30)))), ((int)(((byte)(54)))));
            this.panel1.Controls.Add(this.BtnSatistics);
            this.panel1.Controls.Add(this.BtnStatements);
            this.panel1.Controls.Add(this.BtnLogout);
            this.panel1.Controls.Add(this.BtnAccountBalance);
            this.panel1.Controls.Add(this.BtnProfile);
            this.panel1.Controls.Add(this.panel2);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(200, 690);
            this.panel1.TabIndex = 0;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.PNLNav);
            this.panel2.Controls.Add(this.label1);
            this.panel2.Controls.Add(this.User);
            this.panel2.Controls.Add(this.pictureBox1);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel2.Location = new System.Drawing.Point(0, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(200, 152);
            this.panel2.TabIndex = 0;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::BankingInterface.Properties.Resources.default_profile_picture;
            this.pictureBox1.Location = new System.Drawing.Point(56, 21);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(75, 75);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // User
            // 
            this.User.AutoSize = true;
            this.User.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(126)))), ((int)(((byte)(249)))));
            this.User.Location = new System.Drawing.Point(73, 99);
            this.User.Name = "User";
            this.User.Size = new System.Drawing.Size(30, 15);
            this.User.TabIndex = 1;
            this.User.Text = "User";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(158)))), ((int)(((byte)(161)))), ((int)(((byte)(178)))));
            this.label1.Location = new System.Drawing.Point(56, 123);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 15);
            this.label1.TabIndex = 2;
            this.label1.Text = "=Today()\r\n";
            // 
            // BtnProfile
            // 
            this.BtnProfile.Dock = System.Windows.Forms.DockStyle.Top;
            this.BtnProfile.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.BtnProfile.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(126)))), ((int)(((byte)(249)))));
            this.BtnProfile.Location = new System.Drawing.Point(0, 152);
            this.BtnProfile.Name = "BtnProfile";
            this.BtnProfile.Size = new System.Drawing.Size(200, 48);
            this.BtnProfile.TabIndex = 3;
            this.BtnProfile.Text = "Profile";
            this.BtnProfile.UseVisualStyleBackColor = true;
            this.BtnProfile.Click += new System.EventHandler(this.BtnProfile_Click);
            // 
            // BtnAccountBalance
            // 
            this.BtnAccountBalance.Dock = System.Windows.Forms.DockStyle.Top;
            this.BtnAccountBalance.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.BtnAccountBalance.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(126)))), ((int)(((byte)(249)))));
            this.BtnAccountBalance.Location = new System.Drawing.Point(0, 200);
            this.BtnAccountBalance.Name = "BtnAccountBalance";
            this.BtnAccountBalance.Size = new System.Drawing.Size(200, 48);
            this.BtnAccountBalance.TabIndex = 4;
            this.BtnAccountBalance.Text = "Account Balance";
            this.BtnAccountBalance.UseVisualStyleBackColor = true;
            // 
            // BtnLogout
            // 
            this.BtnLogout.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.BtnLogout.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.BtnLogout.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(126)))), ((int)(((byte)(249)))));
            this.BtnLogout.ImageAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.BtnLogout.Location = new System.Drawing.Point(0, 667);
            this.BtnLogout.Name = "BtnLogout";
            this.BtnLogout.Size = new System.Drawing.Size(200, 23);
            this.BtnLogout.TabIndex = 5;
            this.BtnLogout.Text = "Log out";
            this.BtnLogout.UseVisualStyleBackColor = true;
            // 
            // BtnStatements
            // 
            this.BtnStatements.Dock = System.Windows.Forms.DockStyle.Top;
            this.BtnStatements.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.BtnStatements.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(126)))), ((int)(((byte)(249)))));
            this.BtnStatements.Location = new System.Drawing.Point(0, 248);
            this.BtnStatements.Name = "BtnStatements";
            this.BtnStatements.Size = new System.Drawing.Size(200, 48);
            this.BtnStatements.TabIndex = 6;
            this.BtnStatements.Text = "Statements";
            this.BtnStatements.UseVisualStyleBackColor = true;
            // 
            // BtnSatistics
            // 
            this.BtnSatistics.Dock = System.Windows.Forms.DockStyle.Top;
            this.BtnSatistics.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.BtnSatistics.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(126)))), ((int)(((byte)(249)))));
            this.BtnSatistics.Location = new System.Drawing.Point(0, 296);
            this.BtnSatistics.Name = "BtnSatistics";
            this.BtnSatistics.Size = new System.Drawing.Size(200, 48);
            this.BtnSatistics.TabIndex = 7;
            this.BtnSatistics.Text = "Statistics";
            this.BtnSatistics.UseVisualStyleBackColor = true;
            // 
            // PNLNav
            // 
            this.PNLNav.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(126)))), ((int)(((byte)(249)))));
            this.PNLNav.Location = new System.Drawing.Point(0, 50);
            this.PNLNav.Name = "PNLNav";
            this.PNLNav.Size = new System.Drawing.Size(3, 100);
            this.PNLNav.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(42)))), ((int)(((byte)(52)))), ((int)(((byte)(89)))));
            this.ClientSize = new System.Drawing.Size(1392, 690);
            this.Controls.Add(this.panel1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panel1.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button BtnSatistics;
        private System.Windows.Forms.Button BtnStatements;
        private System.Windows.Forms.Button BtnLogout;
        private System.Windows.Forms.Button BtnAccountBalance;
        private System.Windows.Forms.Button BtnProfile;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel PNLNav;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label User;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

