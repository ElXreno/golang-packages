%global goipath         github.com/issue9/identicon
%global commit          d36b54562f4cf70c83653e13dc95c220c79ef521
%global scm             git

%gometa

%global common_description %{expand:
Generate a beautiful random avatar for the user based on
any data such as the user's IP address and mailbox name.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                A library for generating random avatar based on any data

License:                MIT
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
